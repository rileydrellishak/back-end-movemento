from app.models.journal_entry import JournalEntry
from app.db import db

def test_update_journal_entry(client, user_one, journal_entry_one, movement_one, movement_two, movement_three, movement_four):
    entry_data = {
        'reflection': 'I am updating my reflection!',
        'movements': [1, 3]
    }
    
    response = client.patch('/users/1/entries/1', json=entry_data)

    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 204
    assert updated_entry.reflection == 'I am updating my reflection!'
    assert [m.id for m in updated_entry.movements] == [1, 3]

def test_update_journal_entry_je_invalid_id(client, user_one, journal_entry_one, movement_one, movement_two, movement_three, movement_four):
    entry_data = {
        'reflection': 'I am updating my reflection!',
        'movements': [1, 3]
    }
    
    response = client.patch('/users/1/entries/one', json=entry_data)
    response_body = response.get_json()

    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 400
    assert response_body == {
        'message': 'Id one invalid. Ids must be integers.'
    }
    assert updated_entry.reflection != 'I am updating my reflection!'
    assert [m.id for m in updated_entry.movements] != [1, 3]

def test_update_journal_entry_entry_not_found(client, user_one, journal_entry_one, movement_one, movement_two, movement_three, movement_four):
    entry_data = {
        'reflection': 'I am updating my reflection!',
        'movements': [1, 3]
    }
    
    response = client.patch('/users/1/entries/5', json=entry_data)
    response_body = response.get_json()

    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 404
    assert response_body == {
        'message': 'JournalEntry with id 5 not found.'
    }
    assert updated_entry.reflection != 'I am updating my reflection!'
    assert updated_entry.movements != [1, 3]

def test_update_journal_entry_missing_appropriate_keys(client, user_one, journal_entry_one, movement_one, movement_two, movement_three, movement_four):
    entry_data = {
        'my_feelings': 'a made up key value pair',
        'my_thoughts': [1, 2, 3],
        'reflection': 'new reflection'
    }
    
    response = client.patch('/users/1/entries/1', json=entry_data)

    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 204
    assert not hasattr(updated_entry, 'my_feelings')
    assert not hasattr(updated_entry, 'my_thoughts')
    assert updated_entry.reflection == 'new reflection'

def test_update_journal_entry_nothing_to_update(client, user_one, journal_entry_one):
    entry_data = {}

    response = client.patch('/users/1/entries/1', json=entry_data)
    
    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 204

def test_update_journal_entry_all_keys_not_attr(client, user_one, journal_entry_one):
    entry_data = {
        'my_name': 'Riley',
        'my_birthday': '10'
    }

    response = client.patch('/users/1/entries/1', json=entry_data)
    
    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 204
    assert not hasattr(updated_entry, 'my_name')
    assert not hasattr(updated_entry, 'my_birthday')

def test_update_journal_entry_not_for_user(client, user_one, user_two, journal_entry_one):
    entry_data = {
        'movements': [1, 3],
        'reflection': 'new text'
    }

    response = client.patch('/users/2/entries/1', json=entry_data)
    response_body = response.get_json()

    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 404
    assert response_body == {
        'message': 'Maille does not have a journal entry with ID of 1'
    }
    assert updated_entry.reflection != 'new text'
    assert [m.id for m in updated_entry.movements] != [1, 3]

def test_update_journal_entry_cannot_change_category(client, user_one, user_two, journal_entry_one):
    entry_data = {
        'user_id': 2,
        'created_at': 'now'
    }

    response = client.patch('/users/1/entries/1', json=entry_data)

    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 204
    assert updated_entry.user_id != 4
    assert updated_entry.created_at != 'now'