from app.models.user import User
from app.db import db
import pytest

def test_user_to_dict_method():
    user = User(
        name='Riley'
    )

    user_dict = user.to_dict()
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

    assert user.name == 'Riley'
    assert user.journal_entries ==[]
    assert user.id is None