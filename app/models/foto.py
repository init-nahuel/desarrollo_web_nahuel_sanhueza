from __future__ import annotations

from app.models import Base, Actividad

from sqlalchemy.orm import Mapped, mapped_column, Session, relationship

from sqlalchemy import String, ForeignKey, BigInteger

from typing import Optional, List

from flask import url_for


class Foto(Base):
    __tablename__ = "foto"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    ruta_archivo: Mapped[str] = mapped_column(String(300), nullable=False)
    nombre_archivo: Mapped[str] = mapped_column(String(300), nullable=False)
    actividad_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("actividad.id"), nullable=False)

    actividad: Mapped["Actividad"] = relationship(
        "Actividad", back_populates="fotos")

    @staticmethod
    def get_fotos_by_actividad_id(db: Session, actividad_id) -> List[Optional[Foto]]:
        return db.query(Foto).filter_by(actividad_id=actividad_id).all()

    @staticmethod
    def generate_foto_url(foto: Foto) -> str:
        return url_for("static", filename=f"img/{foto.nombre_archivo}")
