from app.models.user import User
from app.db import db
import pytest

def test_user_to_dict_method():
    user = User(
        id=1,
        name='Riley',
        journal_entries=[]
    )

    user_dict = user.to_dict()
    assert type(user_dict) == dict
    assert user_dict == {
        'id': 1,
        'name': 'Riley',
        'journal_entries': []
    }

@pytest.mark.skip(reason='things are silly')
def test_user_from_dict_method():
    user_data = {
        'name': 'Riley'
    }
    user = User.from_dict(user_data)

    assert user.name == 'Riley'
    assert user.journal_entries ==[]