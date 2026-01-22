from app.models.user import User
from app.db import db
import pytest

def test_user_to_dict_method():
    user = User(
        name='Riley'
    )

    user_dict = user.to_dict()
    
    assert type(user_dict) == dict
    assert user_dict == {
        'id': None,
        'name': 'Riley',
        'journal_entries': []
    }

def test_user_from_dict_method():
    user_data = {
        'name': 'Riley'
    }
    user = User.from_dict(user_data)

    assert type(user) == User
    assert user.id is None
    assert user.name == 'Riley'
    assert user.journal_entries == []

def test_user_from_dict_missing_name():
    user_data = {}
    with pytest.raises(KeyError):
        user = User.from_dict(user_data)

def test_user_from_dict_extra_keys():
    user_data = {
        'name': 'Bixby',
        'birthday': 'August 21'
    }
    user = User.from_dict(user_data)
    assert type(user) == User
    assert not hasattr(user, 'birthday')
    assert user.name == 'Bixby'
    assert user.journal_entries == []