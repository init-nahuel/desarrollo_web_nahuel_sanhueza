from flask import Blueprint, jsonify

from app.db import get_db_session
from app.models import Actividad


estadisticas_routes = Blueprint(
    "estadisticas", __name__, url_prefix="/estadisticas")


@estadisticas_routes.get("/cant_actividades_dia")
def get_cant_actividades_por_dia():
    actividades = []
    with next(get_db_session()) as db:
        actividades = Actividad.get_all_entities(db)
    # TODO: Usar itertools para agrupar por fecha inicio dia y retornar como json
