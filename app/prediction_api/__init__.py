from flask import Blueprint

prediction_api = Blueprint('prediction_api', __name__)

from . import models
