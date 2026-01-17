from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Boolean
from ..db import db
# movement has id, name, slug, category, is_outdoor

class Movement(db.Model):
    __tablename__ = 'movement'
    __tableargs__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    slug: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(30), nullable=False)
    is_outdoor: Mapped[bool] = mapped_column(Boolean, nullable=False)