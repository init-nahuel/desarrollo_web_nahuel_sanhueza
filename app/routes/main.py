from flask import Blueprint, render_template, request

from app.db import get_db_session

from app.models.actividad import Actividad

from app.utilities.parsing import parse_actividades_for_home_page, parse_actividad_to_listado_data

main_routes = Blueprint("main", __name__)


@main_routes.get("/")
def home():
    actividades = []
    with next(get_db_session()) as db:
        actividades = Actividad.get_actividades(db)
        actividades = parse_actividades_for_home_page(db, actividades)

    return render_template("home.html", actividades=actividades)


@main_routes.get("/crear-actividad")
def crear_actividad():
    return render_template("crear-actividad.html")


@main_routes.get("/listado-actividades")
def listado_actividades():
    page = request.args.get("page", 1)
    with next(get_db_session()) as db:
        actividades = Actividad.get_actividades_paginated(db, page)
        actividades_data = list(
            map(lambda a: parse_actividad_to_listado_data(db, a), actividades))
    return render_template("listado-actividades.html", actividades_data=actividades_data)

# foto, actividad,comuna, actividad_tema


@main_routes.get("/detalle-actividad/<int:actividad_id>")
def detalle_actividad(actividad_id: int):

    return render_template("detalle-actividad.html")


@main_routes.get("/estadisticas")
def estadisticas():
    return render_template("estadisticas.html")
