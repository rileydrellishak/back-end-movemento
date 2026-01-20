from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from ..db import db

# users have id, name, journal_entries

class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True)
    
    name: Mapped[str] = mapped_column(String(30))
    # journal_entries - a list of the user's journal entries, populate from journal_entries table