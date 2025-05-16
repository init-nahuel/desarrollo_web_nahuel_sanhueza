from __future__ import annotations

from app.models import Base, Actividad, Region

from sqlalchemy.orm import Mapped, mapped_column, relationship, Session

from sqlalchemy import String, ForeignKey, BigInteger

from typing import List, Optional


class Comuna(Base):
    __tablename__ = "comuna"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    region_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("region.id"), nullable=False)

    actividades: Mapped[List[Actividad]] = relationship(
        "Actividad", back_populates="comuna")
    region: Mapped[Region] = relationship("Region", back_populates="comunas")

    @staticmethod
    def get_comuna_by_nombre(db: Session, nombre: str) -> Optional[Comuna]:
        return db.query(Comuna).filter_by(nombre=nombre).first()
