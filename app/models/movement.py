from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Integer
from app.db import db
from app.models.associations import je_movement_association

# movements have id, name, slug, category, is_outdoor

class Movement(db.Model):
    __tablename__ = 'movement'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True)
    
    name: Mapped[str] = mapped_column(String(30))
    slug: Mapped[str] = mapped_column(String(30))
    category: Mapped[str] = mapped_column(String(30))
    is_outdoor: Mapped[bool] = mapped_column(Boolean)

    journal_entries: Mapped[list['JournalEntry']] = relationship(
        secondary=je_movement_association,
        back_populates='movement'
    )