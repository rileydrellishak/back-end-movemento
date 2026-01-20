from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from app.db import db

# users have id, name, journal_entries

class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True)
    
    name: Mapped[str] = mapped_column(String(30))
    # journal_entries - a list of the user's journal entries, populate from journal_entries table
    journal_entries: Mapped[list['JournalEntry']] = relationship(
        back_populates='user'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'journal_entries': [je.to_dict() for je in self.journal_entries]
        }