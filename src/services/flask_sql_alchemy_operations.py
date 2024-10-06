"""."""

from dataclasses import fields
from typing import Any

from flask_sqlalchemy import SQLAlchemy

from src.protocols.db_add_one_operation import DbAddOneOperation
from src.protocols.db_get_all_operation import DbGetAllOperation
from src.services.base_model import BaseModel


class FlaskSqlAlchemyOperations[T: BaseModel](
    DbAddOneOperation, DbGetAllOperation
):
    """."""

    def __init__(self, model: type[T], db: SQLAlchemy) -> None:
        """."""
        self.__MODEL = model
        self.__DB = db

    def add_one(self, data: dict[str, Any]) -> None:
        """."""
        cleaned_data = {}
        for field in fields(self.__MODEL):
            if field.name not in data:
                continue
            cleaned_data[field.name] = data[field.name]
        self.__DB.session.add(self.__MODEL(**cleaned_data))
        self.__DB.session.commit()

    def get_all(self) -> list[T]:
        """."""
        return self.__DB.session.query(self.__MODEL).all()
