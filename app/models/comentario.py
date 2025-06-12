from __future__ import annotations
import datetime

from app.models import Base, Actividad
from sqlalchemy import String, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import mapped_column, Mapped, relationship, Session
from typing import Optional


class Comentario(Base):
    __tablename__ = "comentario"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    texto: Mapped[str] = mapped_column(String(300), nullable=False)
    fecha: Mapped[datetime.datetime] = mapped_column(
        DateTime(), nullable=False)
    actividad_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("actividad.id"), nullable=False)

    actividad: Mapped[Actividad] = relationship(
        "Actividad", back_populates="comentarios")

    @staticmethod
    def get_comentarios_by_actividad_id(db: Session, actividad_id: int) -> Optional[Comentario]:
        return db.query(Comentario).filter_by(actividad_id=actividad_id).all()
