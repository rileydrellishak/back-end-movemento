from app.models.mood import Mood
from app.db import db
import pytest

def test_user_to_dict_method():
    mood = Mood(
        name='Neutral',
        slug='neutral',
        valence='neutral',
        energy='medium'
    )

    mood_dict = mood.to_dict()
    
    assert type(mood_dict) == dict
    assert mood_dict == {
        'id': None,
        'name': 'Neutral',
        'slug': 'neutral',
        'valence': 'neutral',
        'energy': 'medium'
    }