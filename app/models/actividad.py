import datetime

from app.models.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import String, Integer, DateTime


class Actividad(Base):
    __tablename__ = "actividad"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    comuna: Mapped[int] = mapped_column(Integer())
    sector: Mapped[str] = mapped_column(String(100))
    nombre: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(100))
    celular: Mapped[str] = mapped_column(String(15))
    dia_hora_inicio: Mapped[datetime.datetime] = mapped_column(DateTime())
    dia_hora_termino: Mapped[datetime.datetime] = mapped_column(DateTime())
    descripcion: Mapped[str] = mapped_column(String(500))
