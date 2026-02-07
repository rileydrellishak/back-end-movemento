from flask import Blueprint, request, Response
import requests
from app.models.journal_entry import JournalEntry
from app.utilities.route_utilities import create_model, get_models_with_filters, validate_model
from app.utilities.image_processing import process_image, generate_object_name
from app.services.oci_storage import upload_img_with_par, get_img_with_par, delete_img_from_oci
from app.db import db

bp = Blueprint('journal_entries_bp', __name__, url_prefix='/entries')

@bp.get('')
def get_all_entries():
    return get_models_with_filters(JournalEntry, request.args), 200

@bp.post('/<entry_id>/photo')
def post_photo_for_entry(entry_id):
    if not request.files.get('photo'):
        return {'error': 'No photo provided'}, 400
    entry = validate_model(JournalEntry, entry_id)
    
    if entry.img_path:
        delete_img_from_oci(entry.img_path)
        entry.img_path = None
        
    file = request.files.get('photo')
    processed_img = process_image(file)
    object_name = generate_object_name(entry_id)

    img_path = upload_img_with_par(
        processed_img,
        'image/jpeg',
        object_name
    )
        
    entry.img_path = img_path
    db.session.commit()

    return {'img_path': img_path}, 201

@bp.get('/<entry_id>/photo')
def get_photo_for_entry(entry_id):
    entry = validate_model(JournalEntry, entry_id)
    img_bytes = get_img_with_par(entry.img_path)
    return Response(content=img_bytes, media_type='image/jpeg')