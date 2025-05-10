from __future__ import annotations

from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, Session

from sqlalchemy import String, ForeignKey

from typing import Optional, List

from flask import url_for


class Foto(Base):
    __tablename__ = "foto"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ruta_archivo: Mapped[str] = mapped_column(String(300))
    nombre_archivo: Mapped[str] = mapped_column(String(300))
    actividad_id: Mapped[int] = mapped_column(ForeignKey("actividad.id"))

    @staticmethod
    def get_fotos_by_actividad_id(db: Session, actividad_id) -> List[Optional[Foto]]:
        return db.query(Foto).filter_by(actividad_id=actividad_id).all()

    @staticmethod
    def generate_foto_url(foto: Foto) -> str:
        return url_for("static", filename=f"img/{foto.nombre_archivo}")
