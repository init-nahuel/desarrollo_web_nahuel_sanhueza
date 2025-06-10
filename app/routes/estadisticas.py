from flask import Blueprint, jsonify
import itertools

from app.db import get_db_session
from app.models import Actividad


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
