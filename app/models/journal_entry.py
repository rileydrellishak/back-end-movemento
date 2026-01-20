from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime, Integer
from typing import Optional
from app.db import db
from datetime import datetime

# journal entry has id, movement_type (id of movement, fk), mood before (fk), mood after (fk), reflection, user id, img path, date, time

class JournalEntry(db.Model):
    __tablename__ = 'journal_entry'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    # movements: Mapped[list['Movement']] = 
    # moods_before: Mapped[list['Mood']] = 
    # moods_after: Mapped[list['Mood']] =

    reflection: Mapped[str] = mapped_column(String(511))
    
    # user_id: Mapped['User'] = 
    
    img_path: Mapped[Optional[str]] = mapped_column(
        nullable=True
    )
    
    created_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,

    )