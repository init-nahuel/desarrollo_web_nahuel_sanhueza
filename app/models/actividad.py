from __future__ import annotations

import datetime

from app.models import Base

from sqlalchemy.orm import Mapped, mapped_column, Session, relationship, joinedload

from sqlalchemy import String, DateTime, ForeignKey, BigInteger

from typing import List, Tuple, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models import Comuna, Foto, ContactarPor, ActividadTema, Comentario


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
    contactos: Mapped[List["ContactarPor"]] = relationship(
        "ContactarPor", back_populates="actividad")
    temas: Mapped[List["ActividadTema"]] = relationship(
        "ActividadTema", back_populates="actividad")
    comentarios: Mapped[List["Comentario"]] = relationship(
        "Comentario", back_populates="actividad")

    @staticmethod
    def get_actividades(db: Session, limit: Optional[int] = None) -> List[Actividad]:
        if limit:
            return db.query(Actividad).order_by(Actividad.id.desc()).options(joinedload(Actividad.comuna), joinedload(Actividad.temas), joinedload(Actividad.fotos)).limit(limit).all()

        return db.query(Actividad).order_by(Actividad.id.desc()).options(joinedload(Actividad.comuna), joinedload(Actividad.temas), joinedload(Actividad.fotos)).all()

    @staticmethod
    def get_actividades_paginated(db: Session, page: int, items_per_page: int = 5) -> Tuple[List[Actividad], bool]:
        offset = (page - 1) * items_per_page
        actividades = db.query(Actividad).options(joinedload(Actividad.fotos), joinedload(
            Actividad.comuna), joinedload(Actividad.temas)).offset(offset).limit(items_per_page + 1).all()
        remain = len(actividades) > items_per_page

        return (actividades, remain)

    @staticmethod
    def get_actividad_by_id(db: Session, id: int) -> Optional[Actividad]:
        return db.query(Actividad).filter_by(id=id).options(joinedload(Actividad.fotos), joinedload(Actividad.comuna), joinedload(Actividad.temas), joinedload(Actividad.contactos)).first()
