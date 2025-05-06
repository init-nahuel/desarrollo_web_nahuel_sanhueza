from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import String, ForeignKey


class Foto(Base):
    __tablename__ = "foto"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ruta_archivo: Mapped[str] = mapped_column(String(300))
    nombre_archivo: Mapped[str] = mapped_column(String(300))
    actividad_id: Mapped[int] = mapped_column(ForeignKey("actividad.id"))
