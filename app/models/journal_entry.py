from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime, Integer
from typing import Optional
from app.db import db
from datetime import datetime, timezone
from app.models.associations import je_movement_association, je_mood_before_association, je_mood_after_association

# journal entry has id, movement_type (id of movement, fk), mood before (fk), mood after (fk), reflection, user id, img path, date, time

class JournalEntry(db.Model):
    __tablename__ = 'journal_entry'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    movements: Mapped[list['Movement']] = relationship(
        secondary=je_movement_association,
        back_populates='journal_entries'
    )
    moods_before: Mapped[list['Mood']] = relationship(
        secondary=je_mood_before_association,
        back_populates='je_moods_before'
    )

    moods_after: Mapped[list['Mood']] = relationship(
        secondary=je_mood_after_association,
        back_populates='je_moods_after'
    )

    reflection: Mapped[str] = mapped_column(String(511))
    
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='journal_entries')
    
    img_path: Mapped[Optional[str]] = mapped_column(
        nullable=True
    )
    
    created_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=True
    )