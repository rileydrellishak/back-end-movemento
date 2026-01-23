def test_get_one_user_200(client, user_one, user_two):
    response = client.get('/users/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        'id': 1,
        'name': 'Riley',
        'journal_entries': []
    }

def test_get_user_by_id_400(client, user_one, user_two):
    response = client.get('/users/one')
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {
        'message': 'Id one invalid. Ids must be integers.'
    }

def test_get_user_by_id_404(client, user_one, user_two):
    response = client.get('users/5')
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {
        'message': 'User with id 5 not found.'
        }

def test_get_all_users_with_query_params(client, user_one, user_two, user_three):
    response = client.get('/users?name=bixby')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0]['name'] == 'Bixby'
    assert user_one and user_two not in response_body

def test_get_all_users_sort_by_name(client, user_one, user_two, user_three):
    response = client.get('/users?sort_by=name')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body[0]['name'] == 'Bixby'
    assert response_body[1]['name'] == 'Maille'
    assert response_body[2]['name'] == 'Riley'

def test_get_all_users_sort_by_name_and_direction(client, user_one, user_two, user_three):
    response = client.get('/users?sort_by=name&sort=desc')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body[0]['name'] == 'Riley'
    assert response_body[1]['name'] == 'Maille'
    assert response_body[2]['name'] == 'Bixby'

def test_get_all_users(client, user_one, user_two, user_three):
    response = client.get('/users')
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 3
    assert response_body[0] == user_one.to_dict()
    assert response_body[1] == user_two.to_dict()
    assert response_body[2] == user_three.to_dict()