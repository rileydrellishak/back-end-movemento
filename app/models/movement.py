from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from ..db import db

class Movement(db.Model):
    __tablename__ = 'movements'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    slug: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(30), nullable=False)
    is_outdoor: Mapped[bool] = mapped_column(Boolean, nullable=False)