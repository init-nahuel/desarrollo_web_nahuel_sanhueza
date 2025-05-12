from __future__ import annotations

import enum

from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, Session

from sqlalchemy import Enum, String, ForeignKey

from typing import Optional

from app.models.enums.tema import Tema


class ActividadTema(Base):
    __tablename__ = "actividad_tema"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tema: Mapped[Tema] = mapped_column(
        Enum(Tema, values_callable=lambda obj: [e.value for e in obj]))
    glosa_otro: Mapped[str] = mapped_column(String(15))
    actividad_id: Mapped[int] = mapped_column(ForeignKey("actividad.id"))

    @staticmethod
    def get_actividad_tema_by_actividad_id(db: Session, actividad_id: int) -> Optional[ActividadTema]:
        return db.query(ActividadTema).filter_by(actividad_id=actividad_id).first()
