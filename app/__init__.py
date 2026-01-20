from flask import Flask
from .db import db, migrate
from .models import mood, movement, journal_entry, user
# from .routes import ---
from .routes.user_routes import bp as users_bp
from .routes.journal_entry_routes import bp as entries_bp
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
    app.register_blueprint(users_bp)
    app.register_blueprint(entries_bp)

    return app