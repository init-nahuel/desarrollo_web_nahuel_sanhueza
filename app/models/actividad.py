from __future__ import annotations

import datetime


from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, Session

from sqlalchemy import String, DateTime, ForeignKey

from typing import List, Optional


class Actividad(Base):
    __tablename__ = "actividad"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    comuna_id: Mapped[int] = mapped_column(ForeignKey("comuna.id"))
    sector: Mapped[str] = mapped_column(String(100))
    nombre: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(100))
    celular: Mapped[str] = mapped_column(String(15))
    dia_hora_inicio: Mapped[datetime.datetime] = mapped_column(DateTime())
    dia_hora_termino: Mapped[datetime.datetime] = mapped_column(DateTime())
    descripcion: Mapped[str] = mapped_column(String(500))

    @staticmethod
    def get_actividades(db: Session, limit: int = 10) -> List[Actividad]:
        return db.query(Actividad).limit(limit).all()

    @staticmethod
    def get_actividad_by_id(db: Session, id: int) -> Optional[Actividad]:
        return db.query(Actividad).filter_by(id=id).first()

    @staticmethod
    def get_actividades_paginated(db: Session, page: int, items_per_page: int = 5) -> List[Actividad]:
        offset = (page - 1) * items_per_page
        return db.query(Actividad).offset(offset).limit(items_per_page).all()
