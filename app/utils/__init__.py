import datetime
import app.utils.validations as validations

from typing import Tuple, List

from werkzeug.datastructures import FileStorage


def validate_actividad_data(region: str, comuna: str, sector: str, nombre_organizador: str, email_organizador: str, telefono_organizador: str, medio_contacto: str, identificador: str, dia_hora_inicio: datetime.datetime, dia_hora_termino: datetime.datetime, tema: str, tema_otro: str, fotos: List[FileStorage]) -> Tuple[bool, str]:
    """Valida la informacion enviada en la peticion a la hora de crear una actividad
    """

    if validations.validate_region(region):
        return (False, "Valor de region invalido")
    if validations.validate_comuna(comuna):
        return (False, "Valor de comuna invalido")
    if validations.validate_sector(sector):
        return (False, "Valor de sector invalido")
    if validations.validate_nombre(nombre_organizador):
        return (False, "Valor de nombre organizador invalido")
    if validations.validate_email(email_organizador):
        return (False, "Valor de email organizador invalido")
    if validations.validate_phone_number(telefono_organizador):
        return (False, "Valor de telefono organizador invalido")
    if validations.validate_medio_contacto(medio_contacto, identificador):
        return (False, "Valor de medio contacto invalido")
    if validations.validate_fecha_inicio(dia_hora_inicio):
        return (False, "Valor de fecha inicio invalido")
    if validations.validate_fecha_termino(dia_hora_termino):
        return (False, "Valor de fecha termino invalido")
    if validations.validate_tema(tema, tema_otro):
        return (False, "Valor de tema de actividad invalido")
    if not validations.validate_fotos(fotos):
        return (False, "Fotos invalidas")

    return (True, "")
