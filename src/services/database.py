"""."""

from flask_sqlalchemy import SQLAlchemy
from sqlmodel import SQLModel

from src.services.base_session import BaseSession


class CustomSQLAlchemy(SQLAlchemy):
    """."""

    Model: type[SQLModel]


DB = CustomSQLAlchemy(
    model_class=SQLModel, session_options={"class_": BaseSession}
)
