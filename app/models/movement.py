from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from ..db import db

# movements have id, name, slug, category, is_outdoor

class Movement(db.Model):
    __tablename__ = 'movements'