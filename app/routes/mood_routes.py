from flask import Blueprint, request, Response, abort, make_response
from app.models.mood import Mood
from app.routes.route_utilities import create_model, get_models_with_filters, validate_model
from app.db import db

bp = Blueprint('moods_bp', __name__, url_prefix='/moods')

@bp.get('')
def get_all_moods():
    return get_models_with_filters(Mood, request.args)