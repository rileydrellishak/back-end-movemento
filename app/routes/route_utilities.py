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

def get_models_with_filters(cls, filters=None):
    query = db.select(cls)

    if filters:
        sort_by = filters.get('sort_by', 'title')
        direction = filters.get('sort', None)

        for attribute, value in filters.items():
            if hasattr(cls, attribute):
                query = query.where(getattr(cls, attribute).ilike(f"%{value}%"))

        if hasattr(cls, sort_by):
            sort_column = getattr(cls, sort_by)
            if direction == 'desc':
                query = query.order_by(sort_column.desc())
            else:
                query = query.order_by(sort_column)

    else:
        query = query.order_by(cls.id)

    models = db.session.scalars(query)
    models_response = [model.to_dict() for model in models]
    return models_response

def create_model(cls, data):
    new_model = cls.from_dict(data)

    db.session.add(new_model)
    db.session.commit()
    
    return new_model.to_dict(), 201