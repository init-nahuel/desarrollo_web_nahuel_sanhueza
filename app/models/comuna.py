from app.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import String, ForeignKey, BigInteger


class Comuna(Base):
    __tablename__ = "comuna"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    region_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("region.id"), nullable=False)
