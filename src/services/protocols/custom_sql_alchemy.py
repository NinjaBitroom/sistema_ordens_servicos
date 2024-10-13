"""."""

from flask_sqlalchemy import SQLAlchemy
from sqlmodel import SQLModel


class CustomSQLAlchemy(SQLAlchemy):
    """."""

    Model: type[SQLModel]
