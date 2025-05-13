from sqlalchemy.orm import Session

from app.models import Actividad, ActividadTema, Comuna, Foto

from app.models.data_models.listado_data import ListadoData

from flask import url_for

from typing import List, Any


def parse_actividad_to_listado_data(db: Session, actividad: Actividad) -> ListadoData:
    """Parsea una lista de actividades para generar un objeto de tipo ListadoData, esta clase
    usualmente se utiliza para enviar datos a la pagina listado de actividad los campos de la bd
    que se requieren, tambien se utiliza para enviar los datos a detalle-actividad

    Args:
        actividad (Actividad): Actividad a parsear

    Returns:
        ListadoData: Instancia ListadoData con la informacion de la actividad
    """

    comuna = Comuna.get_entitie_by_id(db, actividad.comuna_id)
    actividad_tema: ActividadTema = ActividadTema.get_actividad_tema_by_actividad_id(
        db, actividad.id)

    fotos = Foto.get_fotos_by_actividad_id(db, actividad.id)
    fotos: List[Foto] = list(filter(lambda f: f is not None, fotos))
    fotos_urls = list(map(Foto.generate_foto_url, fotos))

    listado_data = ListadoData(inicio=actividad.dia_hora_inicio, termino=actividad.dia_hora_termino, comuna=comuna.nombre, sector=actividad.sector, tema=actividad_tema.tema.value,
                               nombre_organizador=actividad.nombre, total_fotos=len(fotos), url=url_for("main.detalle_actividad", actividad_id=actividad.id), fotos_urls=fotos_urls)

    return listado_data
