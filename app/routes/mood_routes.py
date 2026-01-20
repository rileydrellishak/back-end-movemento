from flask import Blueprint
from app.models.mood import Mood
from app.db import db

bp = Blueprint('moods_bp', __name__, url_prefix='/moods')