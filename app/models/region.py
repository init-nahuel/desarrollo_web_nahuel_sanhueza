from __future__ import annotations

from app.models import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship, Session

from sqlalchemy import String, BigInteger

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models import Comuna


class Region(Base):
    __tablename__ = "region"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)

    comunas: Mapped[List["Comuna"]] = relationship(
        "Comuna", back_populates="region")

    @staticmethod
    def get_region_by_name(db: Session, name: str) -> Optional[Region]:
        return db.query(Region).filter_by(nombre=name).first()
