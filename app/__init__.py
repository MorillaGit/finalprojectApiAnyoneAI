from flask import Flask
from flask_cors import CORS
from .credit_api import credit_api


def create_app():
    app = Flask(__name__)
    CORS(app)

    # register blueprints

    app.register_blueprint(credit_api)
    return app
