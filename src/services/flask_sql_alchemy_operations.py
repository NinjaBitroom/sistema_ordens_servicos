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
        self.model = model
        self.db = db

    def add_one(self, data: dict[str, Any]) -> None:
        """."""
        cleaned_data = {}
        for field in fields(self.model):
            if field.name not in data:
                continue
            cleaned_data[field.name] = data[field.name]
        self.db.session.add(self.model(**cleaned_data))
        self.db.session.commit()

    def get_all(self) -> list[T]:
        """."""
        return self.db.session.query(self.model).all()
