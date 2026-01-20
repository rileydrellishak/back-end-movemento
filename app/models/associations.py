from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db import db

je_movement_association = Table(
    'je_movement_association',
    db.metadata,
    Column('je_id', Integer, ForeignKey('journal_entry.id'), primary_key=True),
    Column('movement_id', Integer, ForeignKey('movement.id'), primary_key=True)
)

je_mood_before_association = Table(
    'je_mood_before_association',
    db.metadata,
    Column('je_id', Integer, ForeignKey('journal_entry.id'), primary_key=True),
    Column('mood_id', Integer, ForeignKey('mood.id'), primary_key=True)
)