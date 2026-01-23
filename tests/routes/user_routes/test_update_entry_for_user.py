from app.models.journal_entry import JournalEntry
from app.db import db

def test_update_journal_entry(client, user_one, journal_entry_one):
    entry_data = {
        'reflection': 'I am updating my reflection!'
    }
    
    response = client.patch('/users/1/entries/1', json=entry_data)
    response_body = response.get_json()

    je_query = db.select(JournalEntry).where(JournalEntry.id == 1)
    updated_entry = db.session.scalar(je_query)

    assert response.status_code == 204
    assert updated_entry.reflection == 'I am updating my reflection!'

def test_update_journal_entry_je_invalid_id(client, user_one, journal_entry_one):
    entry_data = {
        'reflection': 'I am updating my reflection!'
    }
    
    response = client.patch('/users/1/entries/one', json=entry_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        'message': 'Id one invalid. Ids must be integers.'
    }
    assert journal_entry_one.reflection != 'I am updating my reflection!'

def test_update_journal_entry_entry_not_found(client, user_one, journal_entry_one):
    entry_data = {
        'reflection': 'I am updating my reflection!'
    }
    
    response = client.patch('/users/1/entries/5', json=entry_data)
    response_body = response.get_json()

    assert response.status_code == 404