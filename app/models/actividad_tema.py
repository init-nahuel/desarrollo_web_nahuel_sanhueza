import enum

from app.models.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import Integer, Enum, String


class Tema(enum.Enum):
    MUSICA = "música"
    DEPORTE = "deporte"
    CIENCIAS = "ciencias"
    RELIGION = "religión"
    POLITICA = "política"
    TECNOLOGIA = "tecnología"
    JUEGOS = "juegos"
    BAILE = "baile"
    COMIDA = "comida"
    OTRO = "otro"


class ActividadTema(Base):
    __tablename__ = "actividad_tema"

    id: Mapped[int] = mapped_column(Integer())
    tema: Mapped[Tema] = mapped_column(Enum(Tema))
    glosa_otro: Mapped[str] = mapped_column(String(15))
    actividad_id: Mapped[int] = mapped_column(Integer())
