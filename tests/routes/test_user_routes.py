from app.models.user import User
from app.models.journal_entry import JournalEntry
from app.models.movement import Movement
from app.models.mood import Mood
from app.db import db
import pytest

def test_get_one_user_by_id(client, user_one, user_two):
    response = client.get('/users/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        'id': 1,
        'name': 'Riley',
        'journal_entries': []
    }

def test_get_user_by_id_invalid_id(client, user_one, user_two):
    response = client.get('/users/one')
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        'message': 'Id one invalid. Ids must be integers.'
    }

def test_get_user_by_id_not_found(client, user_one, user_two):
    response = client.get('users/5')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        'message': 'User with id 5 not found.'
        }

def test_get_all_users(client, user_one, user_two, user_three):
    response = client.get('/users')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body[0] == user_one.to_dict()
    assert response_body[1] == user_two.to_dict()
    assert response_body[2] == user_three.to_dict()

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

def test_get_entries_for_user(client, journal_entry_one, journal_entry_two):
    response = client.get('/users/1/entries')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == journal_entry_one.to_dict()
    assert response_body[1] == journal_entry_two.to_dict()

def test_get_entries_for_user_no_entries(client, user_one, user_two):
    response = client.get('/users/2/entries')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 0

def test_post_entry_for_user(client, user_two, mood_one, mood_two, movement_one, movement_two):
    entry_data = {
        'movements': [movement_one.id, movement_two.id],
        'moods_before': [mood_two.id],
        'moods_after': [mood_one.id],
        'reflection': 'Feeling happy now!',
        'img_path': '/images/1.jpg'
    }

    response = client.post('/users/1/entries', json=entry_data)
    response_body = response.get_json()

    user_query = db.select(User).where(User.id == 1)
    user = db.session.scalar(user_query)

    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    entry = db.session.scalar(je_query)

    assert response.status_code == 201
    assert len(user.journal_entries) == 1

    assert entry
    assert entry.to_dict() == user.journal_entries[0].to_dict()
    for movement in entry.movements:
        assert isinstance(movement, Movement)
    for mood in entry.moods_before:
        assert isinstance(mood, Mood)
    for mood in entry.moods_after:
        assert isinstance(mood, Mood)
    assert entry.created_at

def test_post_entry_for_user_movement_DNE(client, user_two, mood_one, mood_two):
    entry_data = {
        'movements': [3, 4],
        'moods_before': [mood_two.id],
        'moods_after': [mood_one.id],
        'reflection': 'Feeling happy now!',
        'img_path': '/images/1.jpg'
    }

    response = client.post('/users/1/entries', json=entry_data)
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        'message': 'Movement with id 3 not found.'
    }

def test_post_entry_for_user_mood_DNE(client, user_two, movement_one):
    entry_data = {
        'movements': [movement_one.id],
        'moods_before': [2],
        'moods_after': [3],
        'reflection': 'Feeling happy now!',
        'img_path': '/images/1.jpg'
    }

    response = client.post('/users/1/entries', json=entry_data)
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        'message': 'Mood with id 2 not found.'
    }

def test_post_entry_for_user_invalid_datatypes(client, user_two, movement_one, mood_one, mood_two):
    entry_data = {
        'movements': ['one'],
        'moods_before': [mood_two.id],
        'moods_after': [mood_one.id],
        'reflection': 'Feeling happy now!',
        'img_path': '/images/1.jpg'
    }

    response = client.post('/users/1/entries', json=entry_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        'message': f'Id one invalid. Ids must be integers.'
    }