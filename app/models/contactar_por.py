import enum

from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import String, Enum, ForeignKey


class MedioContacto(enum.Enum):
    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"
    X = "X"
    INSTAGRAM = "instagram"
    TIKTOK = "tiktok"
    OTRA = "otra"


class ContactarPor(Base):
    __tablename__ = "contactar_por"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[MedioContacto] = mapped_column(Enum(MedioContacto))
    identificador: Mapped[str] = mapped_column(String(150))
    actividad_id: Mapped[int] = mapped_column(ForeignKey("actividad.id"))
