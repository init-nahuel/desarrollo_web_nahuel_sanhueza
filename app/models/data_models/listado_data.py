from dataclasses import dataclass, field

from datetime import datetime

from typing import Optional, List

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
    fotos_urls: List[str] = field(default=list)
