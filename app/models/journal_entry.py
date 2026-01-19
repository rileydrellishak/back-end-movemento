from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime
from ..db import db
from .associations import journal_entry_movements, journal_entry_moods_before, journal_entry_moods_after
from datetime import datetime

# journal entry has id, movement_type (id of movement, fk), mood before (fk), mood after (fk), reflection, user id, img path, date, time

class JournalEntry(db.Model):
    __tablename__ = 'journal_entries'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    movements: Mapped[list['Movement']] = relationship(
        'Movement',
        secondary=journal_entry_movements,
        backref='journal_entries'
        )
    
    moods_before: Mapped[list['Mood']] = relationship(
        'Mood',
        secondary=journal_entry_moods_before,
        backref='journal_entries'
        )
    
    moods_after: Mapped[list['Mood']] = relationship(
        'Mood',
        secondary=journal_entry_moods_after,
        backref='journal_entries'
    )

    reflection: Mapped[str] = mapped_column(String(1000), nullable=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False
    )

    user: Mapped['User'] = relationship(
        'User',
        back_populates='journal_entries'
    )

    img_path: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.now)