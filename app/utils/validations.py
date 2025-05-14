import re
import datetime

from app.db import get_db_session

from app.models import Region, Comuna, MedioContacto, Tema

PHONE_NUMBER_PATTERN = re.compile(r'^\+569\d{8}$')
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


def validate_min_len_txt(txt: str, limit: int) -> bool:
    return len(txt) >= limit


def validate_max_len_txt(text: str, limit: int) -> bool:
    return len(text) <= limit


def validate_region(region_name: str) -> bool:
    with next(get_db_session()) as db:
        return db.query(Region).filter_by(nombre=region_name).first() is not None


def validate_comuna(comuna_name: str) -> bool:
    with next(get_db_session()) as db:
        return db.query(Comuna).filter_by(nombre=comuna_name).first() is not None


def validate_sector(sector: str) -> bool:
    return validate_max_len_txt(sector, 100)


def validate_nombre(nombre: str) -> bool:
    return nombre != "" and validate_max_len_txt(nombre, 200)


def validate_email(email: str) -> bool:
    return email != "" and validate_max_len_txt(email, 100) and re.fullmatch(EMAIL_PATTERN, email) is not None


def validate_phone_number(phone_number: str) -> bool:
    return re.fullmatch(PHONE_NUMBER_PATTERN, phone_number) is not None


def validate_contactar_por(value: str, identificador: str) -> bool:
    return value in MedioContacto._member_names_ or (value in MedioContacto._member_names_ and validate_max_len_txt(identificador, 50) and validate_min_len_txt(identificador, 4))


# TODO: Verificar formato corrector
def validate_fecha_inicio(fecha_inicio: datetime.datetime) -> bool:
    return fecha_inicio is not None and fecha_inicio > datetime.datetime.now()


def validate_fecha_termino(fecha_termino: datetime.datetime) -> bool:
    return fecha_termino is not None and fecha_termino > datetime.datetime.now()


def validate_tema(tema: str, glosa_otro: str) -> bool:
    return tema in Tema._member_names_ or (tema in Tema._member_names_ and validate_max_len_txt(glosa_otro, 15) and validate_min_len_txt(glosa_otro, 3))


def validate_fotos():
    pass
