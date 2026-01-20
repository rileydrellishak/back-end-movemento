from flask import Blueprint, request
from app.models.user import User
from app.db import db
from app.routes.route_utilities import create_model, get_models_with_filters, validate_model

bp = Blueprint('users_bp', __name__, url_prefix='/users')

@bp.get('')
def get_all_users():
    return get_models_with_filters(User, request.args)

@bp.get('/<id>')
def get_user_by_id(id):
    user = validate_model(User, id)
    return user.to_dict()

@bp.post('')
def create_user():
    user_data = request.get_json()
    return create_model(User, user_data)