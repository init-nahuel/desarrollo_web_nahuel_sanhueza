from __future__ import annotations

import datetime


from app.models.base import Base
from app.models.comuna import Comuna
from app.models.foto import Foto

from sqlalchemy.orm import Mapped, mapped_column, Session, relationship

from sqlalchemy import String, DateTime, ForeignKey, BigInteger

from typing import List, Tuple


class Actividad(Base):
    __tablename__ = "actividad"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    comuna_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("comuna.id"), nullable=False)
    sector: Mapped[str] = mapped_column(String(100))
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    celular: Mapped[str] = mapped_column(String(15))
    dia_hora_inicio: Mapped[datetime.datetime] = mapped_column(
        DateTime(), nullable=False)
    dia_hora_termino: Mapped[datetime.datetime] = mapped_column(
        DateTime(), nullable=False)
    descripcion: Mapped[str] = mapped_column(String(500))

    comuna: Mapped["Comuna"] = relationship(
        "Comuna", back_populates="actividades")
    fotos: Mapped[List["Foto"]] = relationship(
        "Foto", back_populates="actividad")

    @staticmethod
    def get_actividades(db: Session, limit: int = 10) -> List[Actividad]:
        return db.query(Actividad).limit(limit).all()

    @staticmethod
    def get_actividades_paginated(db: Session, page: int, items_per_page: int = 5) -> Tuple[List[Actividad], bool]:
        offset = (page - 1) * items_per_page
        actividades = db.query(Actividad).offset(
            offset).limit(items_per_page + 1).all()
        remain = len(actividades) > items_per_page

        return (actividades, remain)
