from flask import Blueprint
from app.models.user import User
from app.db import db

bp = Blueprint('users_bp', __name__, url_prefix='/users')