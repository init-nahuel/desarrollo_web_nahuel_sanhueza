from app.models.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import String, Integer


class Foto(Base):
    __tablename__ = "foto"

    id: Mapped[int] = mapped_column(Integer())
    ruta_archivo: Mapped[str] = mapped_column(String(300))
    nombre_archivo: Mapped[str] = mapped_column(String(300))
    actividad_id: Mapped[int] = mapped_column(Integer())
