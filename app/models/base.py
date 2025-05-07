from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.inspection import inspect

from typing import Dict, Any


class Base(DeclarativeBase):
    def to_dict(self) -> Dict[str, Any]:
        return {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}
