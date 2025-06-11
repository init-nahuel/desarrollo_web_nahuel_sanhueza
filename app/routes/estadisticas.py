from flask import Blueprint, jsonify
import itertools
from typing import Dict, Any

from app.db import get_db_session
from app.models import Actividad, Tema


estadisticas_routes = Blueprint(
    "estadisticas", __name__, url_prefix="/estadisticas")


@estadisticas_routes.get("/cant_actividades_dia")
def get_cant_actividades_por_dia():
    actividades = []
    with next(get_db_session()) as db:
        actividades = Actividad.get_all_entities(db)
    sorted_actividades = sorted(
        actividades, key=lambda a: a.dia_hora_inicio.date())

    data = []
    for k, g in itertools.groupby(sorted_actividades, key=lambda a: a.dia_hora_inicio.date()):
        val = {k.strftime("%d %b %Y"): len(list(g))}
        data.append(val)
    return jsonify(data)


@estadisticas_routes.get("/total_actividades_tipo")
def get_actividades_por_tipo():
    actividades = []
    with next(get_db_session()) as db:
        actividades = Actividad.get_actividades(db)

    data: Dict[str, Any] = {t.value: 0 for _, t in Tema._member_map_.items()}
    for a in actividades:
        for t in a.temas:
            data[t.tema.value] += 1

    return jsonify(data)
