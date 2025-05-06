from flask import Blueprint, render_template

main_routes = Blueprint("main", __name__)


@main_routes.get("/")
def home():
    return render_template("home.html")


@main_routes.get("/crear-actividad")
def crear_actividad():
    return render_template("crear-actividad.html")


@main_routes.get("/listado-actividades")
def listado_actividades():
    return render_template("listado-actividades.html")


@main_routes.get("/estadisticas")
def estadisticas():
    return render_template("estadisticas.html")
