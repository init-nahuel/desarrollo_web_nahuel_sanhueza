from __future__ import annotations

from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column, Session

from sqlalchemy import String, ForeignKey

from typing import Optional


class Comuna(Base):
    __tablename__ = "comuna"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200))
    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"))

    @staticmethod
    def get_comuna_by_id(db: Session, id: int) -> Optional[Comuna]:
        return db.query(Comuna).filter_by(id=id).first()
