from flask import Flask

def create_app():
    app = Flask(__name__)

    # register blueprints
    from .credit_api import credit_api
    app.register_blueprint(credit_api)

    from .prediction_api import prediction_api
    app.register_blueprint(prediction_api)

    return app
