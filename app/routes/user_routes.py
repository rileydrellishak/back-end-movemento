from flask import Blueprint, request, Response, abort, make_response
from app.models.user import User
from app.models.journal_entry import JournalEntry
from app.routes.route_utilities import create_model, get_models_with_filters, validate_model
from app.db import db

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

@bp.get('/<id>/entries')
def get_entries_for_user(id):
    user = validate_model(User, id)
    response = user.to_dict()
    return response, 200

@bp.post('/<id>/entries')
def post_entry_for_user(id):
    user = validate_model(User, id)
    entry_data = request.get_json()
    entry_data['user_id'] = user.id
    return create_model(JournalEntry, entry_data), 201

@bp.delete('/<user_id>/entries/<entry_id>')
def delete_je_by_id(user_id, entry_id):
    user = validate_model(User, user_id)
    journal_entry = validate_model(JournalEntry, entry_id)

    if journal_entry in set(user.journal_entries):
        db.session.delete(journal_entry)
        db.session.commit()
        return Response(status=204, mimetype='application/json')
    
    else:
        response = {'message': f'{user.name} does not have a journal entry with ID of {entry_id}'}
        abort(make_response(response, 404))