"""."""

from flask_sqlalchemy import SQLAlchemy

from src.protocols.db_add_one_operation import DbAddOneOperation


class FlaskSqlAlchemyOperations[T](DbAddOneOperation):
    """."""

    def __init__(self, model: type[T], db: SQLAlchemy) -> None:
        """."""
        self.model = model
        self.db = db

    def add_one(self, data: T) -> None:
        """."""
        self.db.session.add(data)
        self.db.session.commit()