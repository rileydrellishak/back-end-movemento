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

@pytest.fixture
def one_user(app):
    db.session.add(
        User(name='Riley')
    )

    db.session.commit()

@pytest.fixture
def three_movements(app):
    yoga = Movement(
        name='Yoga',
        slug='yoga',
        category='mind_body',
        is_outdoor=False
    )
    volleyball = Movement(
        name='Volleyball',
        slug='volleyball',
        category='sports',
        is_outdoor=False
    )
    dance = Movement(
        name='Dance',
        slug='dance',
        category='cardio',
        is_outdoor=False
    )
    
    db.session.add_all([yoga, volleyball, dance])
    db.session.commit()