from __future__ import annotations

from app.models.base import Base


from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import String, BigInteger

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.comuna import Comuna


class Region(Base):
    __tablename__ = "region"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)

    comunas: Mapped[List["Comuna"]] = relationship(
        "Comuna", back_populates="region")
