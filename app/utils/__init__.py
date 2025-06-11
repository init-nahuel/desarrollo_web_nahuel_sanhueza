import datetime
import app.utils.validations as validations
import hashlib
import filetype
import os

from flask import current_app as app

from typing import Tuple, List

from werkzeug.utils import secure_filename

from werkzeug.datastructures import FileStorage

from app.models import Region

from app.db import get_db_session


def validate_actividad_data(region: str, comuna: str, sector: str, nombre_organizador: str, email_organizador: str, telefono_organizador: str, medio_contacto: str, identificador: str, dia_hora_inicio: datetime.datetime, dia_hora_termino: datetime.datetime, tema: str, tema_otro: str, fotos: List[FileStorage]) -> Tuple[bool, str]:
    """Valida la informacion enviada en la peticion a la hora de crear una actividad
    """

    if not validations.validate_region(region):
        return (False, "Valor de region invalido")

    with next(get_db_session()) as db:
        region_id = Region.get_region_by_name(db, region).id
    if not validations.validate_comuna(region_id, comuna):
        return (False, "La comuna no corresponde a la misma region")

    if not validations.validate_sector(sector):
        return (False, "Valor de sector invalido")

    if not validations.validate_nombre(nombre_organizador):
        return (False, "Valor de nombre organizador invalido")

    if not validations.validate_email(email_organizador):
        return (False, "Valor de email organizador invalido")

    if not validations.validate_phone_number(telefono_organizador):
        return (False, "Valor de telefono organizador invalido")

    if not validations.validate_medio_contacto(medio_contacto, identificador):
        return (False, "Valor de medio contacto invalido")

    if not validations.validate_fecha_inicio(dia_hora_inicio):
        return (False, "Valor de fecha inicio invalido")

    if not validations.validate_fecha_termino(dia_hora_termino):
        return (False, "Valor de fecha termino invalido")

    if not validations.validate_tema(tema, tema_otro):
        return (False, "Valor de tema de actividad invalido")

    if not validations.validate_fotos(fotos):
        return (False, "Fotos invalidas")

    return (True, "")


def validate_comentario(nombre_comentario: str, comentario: str) -> Tuple[bool, str]:
    """Valida la informacion enviada al momento de registrar un comentario en una actividad

    Args:
        nombre_comentario (str): nombre del usuario que registra el comentario
        comentario (str): comentario

    Returns:
        Tuple[bool, str]: Tupla con valor de validacion de la informacion y razon de rechazo en caso de que la validacion sea incorrecta.
    """
    is_valid = True
    reason = ""
    if len(nombre_comentario) < 3 or len(nombre_comentario) > 80:
        is_valid = False
        reason = "El nombre debe tener entre 3 y 80 caracteres. "
    if len(comentario) < 5:
        is_valid = False
        reason += "El comentario debe tener al menos 5 caracteres."
    return (is_valid, reason)


def save_img(img: FileStorage) -> Tuple[str, str]:
    """Guarda una imagen en el servidor

    Args:
        img (FileStorage): Imagen a guardar

    Returns:
        Tuple[str, str]: Nombre de la imagen y la ruta donde se guardo
    """
    _filename = hashlib.sha256(secure_filename(
        img.filename).encode("utf-8")).hexdigest()
    _extension = filetype.guess(img).extension
    img_filename = f"{_filename}.{_extension}"

    # 2. save img as a file
    img.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

    return (img_filename, app.config["UPLOAD_FOLDER"])
