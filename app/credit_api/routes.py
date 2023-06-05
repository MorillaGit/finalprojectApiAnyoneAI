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

path = "X_train_raw.pkl"

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


def call_prediction_api(credit_info):
    print("test")

    def load_data_checkpoint(path):

        if os.path.exists(path):
            with open(path, "rb") as f:
                filename = pickle.load(f)
                print(f"Object loaded successfully from {path}.")
                return filename
        else:
            return print(f"Object or {path} does not exist.")
    # print pwd
    print("--------",os.getcwd())

    # load data
    dataset = load_data_checkpoint(path)
    print(dataset)
    
    credit_info_dict = vars(credit_info)
    credit_info_json = json.dumps(credit_info_dict)
    # print(credit_info_json)
