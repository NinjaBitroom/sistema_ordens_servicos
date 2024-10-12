"""."""

from flask_sqlalchemy.session import Session as FlaskSQLAlchemySession
from sqlmodel import Session as SQLModelSession


class BaseSession(FlaskSQLAlchemySession, SQLModelSession):
    """."""
