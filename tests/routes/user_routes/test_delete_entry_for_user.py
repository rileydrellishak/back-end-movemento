from app.models.user import User
from app.models.journal_entry import JournalEntry
from app.db import db

def test_delete_journal_entry_by_id_not_users_je(client, user_one, journal_entry_one, journal_entry_two, journal_entry_three):
    response = client.delete('/users/1/entries/3')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'message': 'Riley does not have a journal entry with ID of 3'}

def test_delete_journal_entry_by_id_not_found(client, user_one, journal_entry_one, journal_entry_two, journal_entry_three):
    response = client.delete('/users/1/entries/5')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {'message': 'JournalEntry with id 5 not found.'}

def test_delete_journal_entry_by_id(client, user_one, journal_entry_one, journal_entry_two):
    response = client.delete('users/1/entries/2')
    
    user_query = db.select(User).where(User.id == 1)
    user = db.session.scalar(user_query)

    je_query = db.select(JournalEntry).where(JournalEntry.id == 2)
    je = db.session.scalar(je_query)

    assert response.status_code == 204
    assert len(user.journal_entries) == 1
    assert journal_entry_two not in user.journal_entries
    assert not je