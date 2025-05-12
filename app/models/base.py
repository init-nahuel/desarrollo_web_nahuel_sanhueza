from sqlalchemy.orm import DeclarativeBase, Session

from sqlalchemy.inspection import inspect

from typing import Dict, Any, List, Type, TypeVar

T = TypeVar("T", bound="Base")


class Base(DeclarativeBase):
    def to_dict(self) -> Dict[str, Any]:
        return {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}

    @classmethod
    def get_all_entities(cls: Type[T], db: Session) -> List[T]:
        return db.query(cls).all()
