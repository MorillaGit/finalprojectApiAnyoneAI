from flask import request, jsonify
from . import credit_api
from .models import CreditInfo


import os
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

from typing import Tuple
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder
import json

# path = "X_train_raw.pkl"

# path actual
path = os.path.join(os.path.dirname(__file__), 'X_train_raw.pkl')

@credit_api.route('/credit',methods=['POST'])
def predict_credit():
    data = request.json
    # print(data)
    # validate with the schema
    try:
        credit_info = CreditInfo(**data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    call_prediction_api(credit_info)
    # call prediction api
    return jsonify({'message': 'Successfull POST'})
def load_data_checkpoint(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            filename = pickle.load(f)
            print(f"Object loaded successfully from {path}.")
            return filename
    else:
        return print(f"Object or {path} does not exist.")    


def call_prediction_api(credit_info):
    # print("test")
    # print(path)
    credit_info_dict = vars(credit_info)
    credit_info_json = json.dumps(credit_info_dict)
    # print(credit_info_json)

    dataset = load_data_checkpoint(path)
    # print(dataset)

    # print(type(credit_info_dict))
    # print(credit_info_dict)

    df_to_predict = pd.DataFrame.from_dict(credit_info_dict, orient='index')
    df_to_predict = df_to_predict.transpose()


    # print(dataset.shape, df_to_predict.shape)

    binary_cols=[]
    multi_cols=[]
    categorical_cols = dataset.select_dtypes(include='object').columns.tolist()
    for cat_col in categorical_cols:
            unique_values = dataset[cat_col].nunique()
            if unique_values==1 or unique_values>=20:
                dataset=dataset.drop(cat_col,axis=1)
            if unique_values==2:
                binary_cols.append(cat_col)
            if unique_values>=3 and unique_values<20:
                multi_cols.append(cat_col)

    #  add ID_CLIENT and PAYMENT_DAY to df_to_predict
    df_to_predict['ID_CLIENT'] = 0
    df_to_predict['PAYMENT_DAY'] = 0

    # print(dataset.shape, df_to_predict.shape)


    ord_encoder = OrdinalEncoder()
    for col in binary_cols:
        dataset[col] = ord_encoder.fit_transform(dataset[[col]].fillna('Unknown'))
        df_to_predict[col] = ord_encoder.transform(df_to_predict[[col]].fillna('Unknown')) 

    oh_encoder = OneHotEncoder(handle_unknown="ignore")
    oh_encoder.fit(dataset[multi_cols])

    print(dataset.shape, df_to_predict.shape)

    dataset_cols = oh_encoder.transform(dataset[multi_cols]).toarray()
    df_to_predict_cols = oh_encoder.transform(df_to_predict[multi_cols]).toarray()

    dataset.drop(columns=multi_cols, axis=1, inplace=True)
    df_to_predict.drop(columns=multi_cols, axis=1, inplace=True)    

    dataset = np.concatenate([dataset.to_numpy(), dataset_cols],axis=1)
    df_to_predict = np.concatenate([df_to_predict.to_numpy(), df_to_predict_cols],axis=1)

    #Impute Data for Columns with Missing Data
    imputer=SimpleImputer(missing_values=np.nan,strategy="most_frequent")
    imputer.fit(dataset)

    df_to_predict=imputer.transform(df_to_predict)

    scaler=MinMaxScaler(feature_range=(0,1))
    scaler.fit(dataset)

    df_to_predict=scaler.transform(df_to_predict)

    import mlflow
    import mlflow.pyfunc

    model_path = "93c9d5110ad34c91ac778aa0c88eb2b4/artifacts/lightgbm"  # Reemplaza <RUN_ID> con el ID de la ejecución de tu modelo.
    model_path = os.path.join(os.path.dirname(__file__), model_path)
    model = mlflow.pyfunc.load_model(model_path)

    prediction = model.predict(df_to_predict)

    # Imprimir la predicción
    print("****************",prediction)
