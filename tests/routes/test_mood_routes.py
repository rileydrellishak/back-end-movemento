def test_get_all_moods(client, mood_one, mood_two, mood_three):
    response = client.get('/moods')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body[0] == mood_one.to_dict()
    assert response_body[1] == mood_two.to_dict()
    assert response_body[2] == mood_three.to_dict()

def test_get_all_moods_none_saved(client):
    response = client.get('/moods')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 0

def test_get_one_mood_by_id(client, mood_one, mood_two, mood_three):
    response = client.get('/moods/2')
    response_body = response.get_json()

    assert response.status_code == 200
    assert type(response_body) == dict
    assert response_body == mood_two.to_dict()

def test_get_one_mood_by_id_invalid(client, mood_one, mood_two, mood_three):
    response = client.get('/moods/two')
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        'message': 'Id two invalid. Ids must be integers.'
    }

def test_get_one_mood_by_id_not_found(client, mood_one, mood_two, mood_three):
    response = client.get('/moods/5')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        'message': 'Mood with id 5 not found.'
        }