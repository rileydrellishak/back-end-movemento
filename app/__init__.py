from flask import Flask
from .db import db, migrate
from .models import mood, movement
# from .routes import ---
import os
from flask_cors import CORS
from .config import Config

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints here

    return app