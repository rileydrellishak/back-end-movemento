from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from ..db import db

# moods have id, name, slug, valence, energy

class Mood(db.Model):
    __tablename__ = 'mood'