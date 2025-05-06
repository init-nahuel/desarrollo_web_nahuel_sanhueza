import datetime

from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import String, DateTime, ForeignKey


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
