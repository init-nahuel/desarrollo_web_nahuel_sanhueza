from flask import Blueprint, jsonify
import itertools
import datetime
from typing import Dict, Any

from app.db import get_db_session
from app.models import Actividad, Tema


estadisticas_routes = Blueprint(
    "estadisticas", __name__, url_prefix="/estadisticas")


@estadisticas_routes.get("/actividades_dia")
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


@estadisticas_routes.get("/actividades_tipo")
def get_actividades_por_tipo():
    actividades = []
    with next(get_db_session()) as db:
        actividades = Actividad.get_actividades(db)

    data: Dict[str, Any] = {t.value: 0 for _, t in Tema._member_map_.items()}
    for a in actividades:
        for t in a.temas:
            data[t.tema.value] += 1

    return jsonify(data)


@estadisticas_routes.get("/actividades_jornada_mes")
def get_actividades_jornada_mes():
    actividades = []
    with next(get_db_session()) as db:
        actividades = Actividad.get_all_entities(db)

    sorted_actividades_by_date = sorted(
        actividades, key=lambda a: a.dia_hora_inicio.date())

    data = [
        {
            "name": "Mañana",
            "data": []
        },
        {
            "name": "Mediodia",
            "data": []
        },
        {
            "name": "Tarde",
            "data": []
        }
    ]
    meses = []
    for k, g in itertools.groupby(sorted_actividades_by_date, key=lambda a: (a.dia_hora_inicio.date().year, a.dia_hora_inicio.date().month)):
        meses.append(datetime.date(k[0], k[1], 1).strftime("%b %Y"))

        actividades_jornada_am = list(
            filter(lambda a: a.dia_hora_inicio.hour >= 0 and a.dia_hora_inicio.hour < 12, g))
        actividades_jornada_mid = list(
            filter(lambda a: a.dia_hora_inicio.hour >= 12 and a.dia_hora_inicio.hour < 13, g))
        actividades_jornada_pm = list(
            filter(lambda a: a.dia_hora_inicio.hour >= 13 and a.dia_hora_inicio.hour <= 24, g))

        data[0]["data"].append(len(actividades_jornada_am))
        data[1]["data"].append(len(actividades_jornada_mid))
        data[2]["data"].append(len(actividades_jornada_pm))

    return jsonify({
        "meses": meses,
        "series": data
    })
