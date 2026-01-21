from flask import Blueprint, request, Response, abort, make_response
from app.models.movement import Movement
from app.routes.route_utilities import create_model, get_models_with_filters, validate_model
from app.db import db

bp = Blueprint('movements_bp', __name__, url_prefix='/movements')

@bp.get('')
def get_all_movements():
    return get_models_with_filters(Movement, request.args)