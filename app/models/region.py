from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import String, BigInteger


class Region(Base):
    __tablename__ = "region"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
