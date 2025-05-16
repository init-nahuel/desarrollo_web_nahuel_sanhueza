from __future__ import annotations

from app.models import Base, Actividad, MedioContacto

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import String, Enum, ForeignKey, BigInteger


class ContactarPor(Base):
    __tablename__ = "contactar_por"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    nombre: Mapped[MedioContacto] = mapped_column(
        Enum(MedioContacto, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    identificador: Mapped[str] = mapped_column(String(150), nullable=False)
    actividad_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("actividad.id"), nullable=False)

    actividad: Mapped["Actividad"] = relationship(
        "Actividad", back_populates="contactos")
