from app.models.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import String, Integer


class Region(Base):
    __tablename__ = "region"

    id: Mapped[int] = mapped_column(Integer())
    nombre: Mapped[str] = mapped_column(String(200))
