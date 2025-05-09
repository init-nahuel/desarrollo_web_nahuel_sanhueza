from sqlalchemy.orm import Session

from app.models.actividad import Actividad
from app.models.actividad_tema import ActividadTema
from app.models.comuna import Comuna
from app.models.foto import Foto

from flask import url_for

from typing import List, Dict, Any


def parse_actividades_for_home_page(db: Session, actividades: List[Actividad]) -> List[Dict[str, Any]]:
    """Parsea una lista de actividades para generar una lista de diccionarios con la informacion de la actividad
     y llaves para el nombre de la comuna, tema y foto de la actividad requeridos por la tabla 
     de la pagina home

    Args:
        actividades (List[Actividad]): Lista de actividades a parsear              

    Returns:
        List[Dict[str, Any]]: Lista de diccionarios con la informacion de la actividad
    """

    data_dict = []

    for actividad in actividades:
        comuna = Comuna.get_comuna_by_id(db, actividad.comuna_id)
        tema = ActividadTema.get_actividad_tema_by_actividad_id(
            db, actividad.id)

        fotos = Foto.get_fotos_by_actividad_id(db, actividad.id)
        first_foto_filename = ""
        if len(fotos) > 0:
            first_foto = fotos[0]
            first_foto_filename = first_foto.nombre_archivo

        data_dict.append({
            "inicio": actividad.dia_hora_inicio,
            "termino": actividad.dia_hora_termino,
            "comuna": comuna.nombre,
            "sector": actividad.sector,
            "tema": tema.tema.value,
            "url_foto": url_for("static", filename=f"img/{first_foto_filename}")
        })

    return data_dict
