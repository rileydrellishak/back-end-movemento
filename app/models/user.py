from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from ..db import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=False)
    journal_entries: Mapped[list['JournalEntry']] = relationship(
        'JournalEntry',
        back_populates='user'
    )