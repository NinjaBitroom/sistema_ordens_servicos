"""."""

from flask import Flask

from src.services.extensions.database import DB
from src.services.extensions.migrations import ALEMBIC


def init_app(app: Flask) -> None:
    """."""
    DB.init_app(app)
    ALEMBIC.init_app(app)
