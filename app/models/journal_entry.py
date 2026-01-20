from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime
from app.db import db
from datetime import datetime

# journal entry has id, movement_type (id of movement, fk), mood before (fk), mood after (fk), reflection, user id, img path, date, time

class JournalEntry(db.Model):
    __tablename__ = 'journal_entry'