from app.models.movement import Movement
from app.db import db
import pytest

def test_get_all_movements(client, movement_one, movement_two):
    response = client.get('/movements')
    response_body = response.get_json()

    assert type(response_body) == list
    assert len(response_body) == 2
    assert response_body[0] == {
        'id': 1,
        'name': 'Yoga',
        'slug': 'yoga',
        'category': 'mind_body',
        'is_outdoor': False
    }

    assert response_body[1] == {
        'id': 2,
        'name': 'Volleyball',
        'slug': 'volleyball',
        'category': 'sports',
        'is_outdoor': False
    }

def test_get_one_movement(client, movement_one, movement_two, movement_three):
    response = client.get('/movements/2')
    response_body = response.get_json()

    assert response_body == {
        'id': 2,
        'name': 'Volleyball',
        'slug': 'volleyball',
        'category': 'sports',
        'is_outdoor': False
    }

def test_get_one_movement_invalid_id(client, movement_one, movement_two, movement_three):
    response = client.get('/movements/two')
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        'message': f'Id two invalid. Ids must be integers.'
        }
    
def test_get_one_movement_id_not_found(client, movement_one, movement_two, movement_three):
    response = client.get('/movements/5')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        'message': 'Movement with id 5 not found.'
        }