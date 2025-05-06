from app.models.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import String, Integer


class Comuna(Base):
    __tablename__ = "comuna"

    id: Mapped[int] = mapped_column(Integer())
    nombre: Mapped[str] = mapped_column(String(200))
    region: Mapped[int] = mapped_column(Integer())
