from __future__ import annotations

from app.models.base import Base
from app.models.actividad import Actividad

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import String, ForeignKey, BigInteger

from typing import List


class Comuna(Base):
    __tablename__ = "comuna"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    region_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("region.id"), nullable=False)

    actividades: Mapped[List[Actividad]] = relationship(
        "Actividad", back_populates="comuna")
