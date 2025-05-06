from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import String


class Region(Base):
    __tablename__ = "region"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200))
