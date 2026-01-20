from flask import Blueprint, request
from app.models.journal_entry import JournalEntry
from app.routes.route_utilities import create_model, get_models_with_filters, validate_model

bp = Blueprint('journal_entries_bp', __name__, url_prefix='/entries')

@bp.get('')
def get_all_entries():
    return get_models_with_filters(JournalEntry, request.args)