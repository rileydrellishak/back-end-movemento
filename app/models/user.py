from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from ..db import db

# users have id, name, journal_entries

class User(db.Model):
    __tablename__ = 'users'