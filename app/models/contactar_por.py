import enum

from app.models.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import String, Integer, Enum


class MedioContacto(enum.Enum):
    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"
    X = "X"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    OTRA = "otra"


class ContactarPor(Base):
    __tablename__ = "contactar_por"

    id: Mapped[int] = mapped_column(Integer())
    nombre: Mapped[MedioContacto] = mapped_column(Enum(MedioContacto))
    identificador: Mapped[str] = mapped_column(String(150))
    actividad_id: Mapped[int] = mapped_column(Integer())
