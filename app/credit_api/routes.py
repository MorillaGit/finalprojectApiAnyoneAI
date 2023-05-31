from flask import request, jsonify
from . import credit_api
from .models import CreditInfo

@credit_api.route('/credit',methods=['POST'])
def predict_credit():
    data = request.json
    print(data)
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
