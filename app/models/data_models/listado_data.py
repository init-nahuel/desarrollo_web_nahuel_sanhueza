from dataclasses import dataclass

from datetime import datetime

from typing import Optional

from app.models.data_models.base_data_model import BaseDataModel


@dataclass
class ListadoData(BaseDataModel):
    inicio: Optional[datetime] = None
    termino: Optional[datetime] = None
    comuna: str = ""
    sector: str = ""
    tema: str = ""
    nombre_organizador: str = ""
    total_fotos: int = 0
    url: str = ""
