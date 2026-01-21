from app.models.user import User
from app.db import db
import pytest

def test_get_one_user(client, user_one):
    response = client.get('/users/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        'id': 1,
        'name': 'Riley',
        'journal_entries': []
    }

@pytest.mark.skip(reason='things are silly')
def test_create_one_user(client):
    user_data = {
        'name': 'Riley'
    }
    response = client.post('/users', json=user_data)
    response_body = response.get_json()

    assert response.status_code == 201