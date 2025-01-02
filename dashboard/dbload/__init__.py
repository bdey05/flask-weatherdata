from flask import Blueprint

bp = Blueprint('dbload', __name__)

from dashboard.dbload import routes 