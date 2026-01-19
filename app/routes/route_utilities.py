from flask import abort, make_response
from ..db import db

def validate_model(cls, id):
    try:
        model_id = int(id)
        
    except:
        response = {'message': f'Id {id} invalid. Ids must be integers.'}
        abort(make_response(response, 400))
    
    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {'message': f'{cls.__name__} with id {model_id} not found.'}
        abort(make_response(response, 404))
    
    return model