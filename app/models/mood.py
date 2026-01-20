from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from .associations import journal_entry_moods_before, journal_entry_moods_after
from ..db import db

class Mood(db.Model):
    __tablename__ = 'moods'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    slug: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    valence: Mapped[str] = mapped_column(String(20), nullable=False)
    energy: Mapped[str] = mapped_column(String(20), nullable=False)