from flask import Blueprint
from app.models.user import User
from app.db import db

bp = Blueprint('users_bp', __name__, url_prefix='/users')

@bp.get('')
def get_all_users():
    query = db.select(User)
    users = db.session.scalars(query)
    response = []
    for user in users:
        response.append(user.to_dict())
    return response