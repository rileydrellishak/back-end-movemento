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