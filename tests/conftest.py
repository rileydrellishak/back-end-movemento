import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.mood import Mood
from app.models.journal_entry import JournalEntry
from app.models.movement import Movement
from app.models.user import User

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }

    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

# User fixtures
@pytest.fixture
def user_one(app):
    riley = User(name='Riley')

    db.session.add(riley)
    db.session.commit()

    return riley

@pytest.fixture
def user_two(app):
    maille = User(name='Maille')

    db.session.add(maille)
    db.session.commit()

    return maille

@pytest.fixture
def user_three(app):
    bixby = User(name='Bixby')

    db.session.add(bixby)
    db.session.commit()

    return bixby

# Movement fixtures
@pytest.fixture
def movement_one(app):
    yoga = Movement(
        name='Yoga',
        slug='yoga',
        category='mind_body',
        is_outdoor=False
    )
    
    db.session.add(yoga)
    db.session.commit()

    return yoga

@pytest.fixture
def movement_two(app):
    volleyball = Movement(
        name='Volleyball',
        slug='volleyball',
        category='sports',
        is_outdoor=False
    )

    db.session.add(volleyball)
    db.session.commit()

    return volleyball

@pytest.fixture
def movement_three(app):
    dance = Movement(
        name='Dance',
        slug='dance',
        category='cardio',
        is_outdoor=False
    )

    db.session.add(dance)
    db.session.commit()

    return dance

@pytest.fixture
def movement_four(app):
    outdoor_walk = Movement(
        name='Outdoor Walk',
        slug='outdoor_walk',
        category='cardio',
        is_outdoor=True
    )

    db.session.add(outdoor_walk)
    db.session.commit()

    return outdoor_walk

# Mood fixtures
@pytest.fixture
def mood_one(app):
    happy = Mood(
        name='Happy',
        slug='happy',
        valence='positive',
        energy='medium'
    )

    db.session.add(happy)
    db.session.commit()

    return happy

@pytest.fixture
def mood_two(app):
    sad = Mood(
        name='Sad',
        slug='sad',
        valence='negative',
        energy='low'
    )

    db.session.add(sad)
    db.session.commit()

    return sad

@pytest.fixture
def mood_three(app):
    neutral = Mood(
        name='Neutral',
        slug='neutral',
        valence='neutral',
        energy='medium'
    )

    db.session.add(neutral)
    db.session.commit()

    return neutral

@pytest.fixture
def mood_four(app):
    energized = Mood(
        name='Energized',
        slug='energized',
        valence='positive',
        energy='high'
    )

    db.session.add(energized)
    db.session.commit()

    return energized

# Journal Entry fixtures
@pytest.fixture
def journal_entry_one(app, user_one, mood_one, mood_two, movement_one, movement_two):
    # user 1 is Riley
    # mood 1 is happy
    # mood 2 is sad
    # movement 1 is yoga
    # movement 2 is volleyball

    journal_entry = JournalEntry(
        movements=[movement_one, movement_two],
        moods_before=[mood_two],
        moods_after=[mood_one],
        reflection='Feeling so much better!',
        user_id=user_one.id,
        img_path='/images/1.jpg',
    )

    db.session.add(journal_entry)
    db.session.commit()

    return journal_entry

@pytest.fixture
def journal_entry_two(app, user_one, mood_one, mood_three, movement_three, movement_four):
    # user 1 is Riley
    # mood 1 is happy
    # mood 2 is sad
    # movement 1 is yoga
    # movement 2 is volleyball

    journal_entry = JournalEntry(
        movements=[movement_three, movement_four],
        moods_before=[mood_three],
        moods_after=[mood_one],
        reflection='My mood is way better than neutral now',
        user_id=user_one.id,
        img_path='/images/2.jpg',
    )

    db.session.add(journal_entry)
    db.session.commit()

    return journal_entry