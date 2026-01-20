from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from app.db import db

# moods have id, name, slug, valence, energy

class Mood(db.Model):
    __tablename__ = 'mood'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(String(30))
    slug: Mapped[str] = mapped_column(String(30))
    valence: Mapped[str] = mapped_column(String(30))
    energy: Mapped[str] = mapped_column(String(30))