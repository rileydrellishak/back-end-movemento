from app.models.user import User
from app.db import db
import pytest

def test_get_one_user(client, one_user):
    response = client.get('/users/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        'id': 1,
        'name': 'Riley',
        'journal_entries': []
    }