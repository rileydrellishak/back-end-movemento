from flask import Blueprint
from app.models.mood import Mood
from app.db import db

bp = Blueprint('moods_bp', __name__, url_prefix='/moods')

@bp.get('')
def get_all_moods():
    query = db.select(Mood)
    moods = db.session.scalars(query)
    response = []
    for mood in moods:
        response.append(mood.to_dict())
    return response