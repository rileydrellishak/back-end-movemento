from flask import Blueprint, request
import requests
from app.models.journal_entry import JournalEntry
from app.utilities.route_utilities import create_model, get_models_with_filters, validate_model, process_image
import uuid

bp = Blueprint('journal_entries_bp', __name__, url_prefix='/entries')

@bp.get('')
def get_all_entries():
    return get_models_with_filters(JournalEntry, request.args), 200

@bp.post('/<entry_id>/photo')
def post_photo_for_entry(entry_id):
    # receive image file
    # upload image to oci object storage
    # get object url from oci os
    # save url string to db - get the journal entry and assign url to img_path
    # return url to front end
    file = request.files.get('photo')
    if not file:
        return {'message': 'no file uploaded'}, 204
    
    resized_img = process_image(file)
    headers = {
        'Content-Type': 'image/jpg'
    }
    object_name = f'entries/{entry_id}/{uuid.uuid4()}.jpg'