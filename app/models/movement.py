from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Integer
from app.db import db

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