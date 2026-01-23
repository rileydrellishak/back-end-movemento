from app.models.journal_entry import JournalEntry
from app.db import db

def test_update_journal_entry(client, user_one, journal_entry_one, movement_one, movement_two, movement_three, movement_four):
    entry_data = {
        'reflection': 'I am updating my reflection!',
        'movements': [1, 3]
    }
    
    response = client.patch('/users/1/entries/1', json=entry_data)
    response_body = response.get_json()

    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 204
    assert updated_entry.reflection == 'I am updating my reflection!'
    assert updated_entry.movements == [1, 3]

def test_update_journal_entry_je_invalid_id(client, user_one, journal_entry_one, movement_one, movement_two, movement_three, movement_four):
    entry_data = {
        'reflection': 'I am updating my reflection!',
        'movements': [1, 3]
    }
    
    response = client.patch('/users/1/entries/one', json=entry_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        'message': 'Id one invalid. Ids must be integers.'
    }
    assert journal_entry_one.reflection != 'I am updating my reflection!'
    assert journal_entry_one.movements != [1, 2]

def test_update_journal_entry_entry_not_found(client, user_one, journal_entry_one, movement_one, movement_two, movement_three, movement_four):
    entry_data = {
        'reflection': 'I am updating my reflection!',
        'movements': [1, 3]
    }
    
    response = client.patch('/users/1/entries/5', json=entry_data)
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        'message': 'JournalEntry with id 5 not found.'
    }
    assert journal_entry_one.reflection != 'I am updating my reflection!'
    assert journal_entry_one.movements != [1, 3]

def test_update_journal_entry_missing_appropriate_keys(client, user_one, journal_entry_one, movement_one, movement_two, movement_three, movement_four):
    entry_data = {
        'my feelings': 'a made up key value pair',
        'my thoughts': [1, 2, 3],
        'reflection': 'new reflection'
    }
    
    response = client.patch('/users/1/entries/1', json=entry_data)
    response_body = response.get_json()

    assert response.status_code == 204
    assert not hasattr(journal_entry_one, 'my feelings')
    assert not hasattr(journal_entry_one, 'my thoughts')
    assert journal_entry_one.reflection == 'new reflection'

def test_update_journal_entry_nothing_to_update(client, user_one, journal_entry_one):
    entry_data = {}

    response = client.patch('/users/1/entries/1', json=entry_data)
    response_body = response.get_json()

    assert response.status_code == 204