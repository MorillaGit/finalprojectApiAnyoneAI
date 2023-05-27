from flask import request, jsonify
from . import credit_api

@credit_api.route('/credit', methods=['POST'])
def predict_credit():
    # Obtener el JSON enviado en el request
    credit_info = request.json

    # Llamar a la otra API de predicción
    prediction = call_prediction_api(credit_info)
    print("test")
    # Devolver la respuesta como un JSON
    return jsonify(prediction)

def call_prediction_api(credit_info):
    print("test")
    # Aquí debes implementar la lógica para llamar a la otra API de predicción
    # utilizando la información de crédito recibida en el JSON.

    # Por ejemplo:
    # import requests
