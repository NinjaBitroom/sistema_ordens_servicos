"""."""

from pathlib import Path

from flask import Flask

from src.main.config.db import create_tables
from src.main.config.env import configure_env
from src.main.config.routes import setup_routes
from src.services.database import DB


def create_app() -> Flask:
    """."""
    app = Flask(__name__, template_folder=Path("src", "templates").absolute())
    setup_routes(app)
    configure_env(app)
    DB.init_app(app)
    create_tables(app, DB)
    return app
