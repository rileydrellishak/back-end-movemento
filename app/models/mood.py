from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from app.db import db
from app.models.associations import je_mood_before_association, je_mood_after_association

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

    je_moods_before: Mapped[list['JournalEntry']] = relationship(
        secondary=je_mood_before_association,
        back_populates='movement'
    )

    je_moods_after: Mapped[list['JournalEntry']] = relationship(
        secondary=je_mood_after_association,
        back_populates='movement'
    )