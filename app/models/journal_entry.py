from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime, Integer, select
from typing import Optional
from app.db import db
from datetime import datetime, timezone
from app.models.associations import je_movement_association, je_mood_before_association, je_mood_after_association
from app.models.movement import Movement
from app.models.mood import Mood
from app.models.user import User

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

    @classmethod
    def from_dict(cls, entry_data):
        entry_data['created_at'] = entry_data.get('created_at', datetime.now(tz=None))

        movement_ids = entry_data.get('movements', [])
        moods_before_ids = entry_data.get('moods_before', [])
        moods_after_ids = entry_data.get('moods_after', [])

        movements = db.session.scalars(
            select(Movement)
            .where(Movement.id.in_(set(movement_ids)))
            ).all() if movement_ids else []
        
        moods_before = db.session.scalars(
            select(Mood)
            .where(Mood.id.in_(set(moods_before_ids)))
            ).all() if moods_before_ids else []
        
        moods_after = db.session.scalars(
            select(Mood)
            .where(Mood.id.in_(set(moods_after_ids)))
            ).all() if moods_after_ids else []
        
        user = db.session.scalar(
            select(User)
            .where(User.id == entry_data['user_id'])
        )
        
        new_entry = JournalEntry(
            movements=movements,
            moods_before=moods_before,
            moods_after=moods_after,
            reflection=entry_data['reflection'],
            created_at=entry_data['created_at'],
            img_path=entry_data.get('img_path', None),
            user_id=user.id
        )

        return new_entry
    
    def to_dict(self):
        return {
            'id': self.id,
            'movements': [movement.to_dict() for movement in self.movements],
            'moods_before': [mood.to_dict() for mood in self.moods_before],
            'moods_after': [mood.to_dict() for mood in self.moods_after],
            'reflection': self.reflection,
            'user_id': self.user_id,
            'img_path': self.img_path,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }