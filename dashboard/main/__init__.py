from flask import Blueprint

bp = Blueprint('main', __name__)

from dashboard.main import routes 