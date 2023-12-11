# /auth/__ini__.py
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
