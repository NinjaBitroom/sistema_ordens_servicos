"""."""

from collections.abc import Mapping
from typing import Any

from flask_sqlalchemy import SQLAlchemy
from sqlmodel import SQLModel

from src.protocols.db.db_add_one_operation import DbAddOneOperation
from src.protocols.db.db_get_all_operation import DbGetAllOperation
from src.protocols.db.db_get_one_operation import DbGetOneOperation
from src.protocols.db.db_update_operation import DbUpdateOperation
from src.protocols.db.update_data import UpdateData


class FlaskSqlAlchemyOperations[T: SQLModel](
    DbAddOneOperation,
    DbGetAllOperation[T],
    DbGetOneOperation[T],
    DbUpdateOperation[T],
):
    """."""

    def __init__(self, model: type[T], db: SQLAlchemy) -> None:
        """."""
        self.__MODEL = model
        self.__DB = db

    def add_one(self, data: Mapping[str, Any]) -> None:
        """."""
        cleaned_data = {}
        for field in self.__MODEL.model_fields:
            if data.get(field) is None:
                continue
            if isinstance(data[field], SQLModel):
                cleaned_data[f"{field}_id"] = data[field].id
            cleaned_data[field] = data[field]
        self.__DB.session.add(self.__MODEL(**cleaned_data))
        self.__DB.session.commit()

    def get_all(self) -> list[T]:
        """."""
        return self.__DB.session.query(self.__MODEL).all()

    def get_one(self, data: Mapping[Any, Any]) -> T:
        """."""
        return self.__DB.session.query(self.__MODEL).filter_by(**data).one()

    def update(self, data: UpdateData[T]) -> None:
        """."""
        for key, value in data.data.items():
            setattr(data.object, key, value)
        self.__DB.session.commit()
