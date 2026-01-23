from app.models.journal_entry import JournalEntry
from app.models.movement import Movement
from app.models.mood import Mood
import pytest

movement = Movement(
        name='Dance',
        slug='dance',
        category='cardio',
        is_outdoor=False
    )
mood_before = Mood(
        name='Neutral',
        slug='neutral',
        valence='neutral',
        energy='medium'
    )
mood_after = Mood(
        name='Happy',
        slug='happy',
        valence='positive',
        energy='medium'
    )

def test_journal_entry_to_dict():
    entry = JournalEntry(
        movements=[movement],
        moods_before=[mood_before],
        moods_after=[mood_after],
        reflection='Amazing dance session!',
        user_id=1,
        img_path='/images/dance_001.jpg',
    )

    entry_dict = entry.to_dict()

    assert entry_dict['reflection'] == 'Amazing dance session!'
    assert entry_dict['user_id'] == 1
    

def test_journal_entry_from_dict():
    entry_data = {
        'movements': [movement],
        'moods_before': [mood_before],
        'moods_after': [mood_after],
        'reflection': 'Amazing dance session!',
        'user_id': 1,
        'img_path': '/images/dance_001.jpg'
    }

    entry = JournalEntry.from_dict(entry_data)

    assert isinstance(entry.movements[0], Movement)
    assert isinstance(entry.moods_before[0], Mood)
    assert isinstance(entry.moods_after[0], Mood)
    assert entry.reflection == 'Amazing dance session!'
    assert entry.user_id == 1
    assert entry.img_path == '/images/dance_001.jpg'
    assert entry.created_at

def test_journal_entry_from_dict_missing_keys():
    entry_data = {
        'moods_after': [mood_after],
        'reflection': 'Amazing dance session!',
        'user_id': 1,
        'img_path': '/images/dance_001.jpg'
    }
    with pytest.raises(KeyError):
        entry = JournalEntry.from_dict(entry_data)

def test_journal_entry_from_dict_missing_optional_keys():
    entry_data = {
        'movements': [movement],
        'moods_before': [mood_before],
        'moods_after': [mood_after],
        'user_id': 1,
    }

    entry = JournalEntry.from_dict(entry_data)

    assert entry
    assert entry.reflection is None
    assert entry.img_path is None

def test_journal_entry_from_dict_extra_keys_are_skipped():
    entry_data = {
        'movements': [movement],
        'moods_before': [mood_before],
        'moods_after': [mood_after],
        'reflection': 'Amazing dance session!',
        'user_id': 1,
        'img_path': '/images/dance_001.jpg',
        'extra_1': 'heyyy',
        'extra_2': 'hiii'
    }

    entry = JournalEntry.from_dict(entry_data)

    assert entry
    assert not hasattr(entry, 'extra_1')
    assert not hasattr(entry, 'extra_2')