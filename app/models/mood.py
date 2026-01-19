from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Integer
from ..db import db

class Mood(db.Model):
    __tablename__ = 'moods'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    slug: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    valence: Mapped[str] = mapped_column(String(20), nullable=False)
    energy: Mapped[str] = mapped_column(String(20), nullable=False)