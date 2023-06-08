from flask import Blueprint

credit_api = Blueprint('credit_api', __name__)

from . import routes

