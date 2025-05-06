from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import String, ForeignKey


class Comuna(Base):
    __tablename__ = "comuna"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200))
    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"))
