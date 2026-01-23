from app.models.user import User
from app.db import db
import pytest

def test_create_one_user(client):
    user_data = {
        'name': 'Riley'
    }
    response = client.post('/users', json=user_data)
    response_body = response.get_json()

    query = db.select(User).where(User.id == 1)
    new_user = db.session.scalar(query)

    assert response.status_code == 201
    assert response_body == {
        'id': 1,
        'name': 'Riley',
        'journal_entries': []
    }
    assert new_user
    assert new_user.id == 1
    assert new_user.name == 'Riley'
    assert new_user.journal_entries == []

def test_create_one_user_missing_required_keys(client):
    user_data = {}
    
    with pytest.raises(KeyError, match = 'name'):
        new_user = User.from_dict(user_data)

def test_create_one_user_extra_keys(client):
    user_data = {
        'name': 'Riley',
        'birthday': 'November 10'
    }

    response = client.post('/users', json=user_data)
    response_body = response.get_json()

    query = db.select(User).where(User.id == 1)
    new_user = db.session.scalar(query)

    assert response.status_code == 201
    assert response_body == {
        'id': 1,
        'name': 'Riley',
        'journal_entries': []
    }

    assert new_user
    assert new_user.id == 1
    assert new_user.name == 'Riley'
    assert new_user.journal_entries == []
    assert not hasattr(new_user, 'birthday')