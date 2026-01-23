from app.models.user import User
from app.models.journal_entry import JournalEntry
from app.models.movement import Movement
from app.models.mood import Mood
from app.db import db

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