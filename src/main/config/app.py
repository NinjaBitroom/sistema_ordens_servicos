"""."""

from pathlib import Path

from flask import Flask

from src.main.config.env import configure_env
from src.main.config.extensions import init_app
from src.main.config.routes import setup_routes


def create_app() -> Flask:
    """."""
    app = Flask(__name__, template_folder=Path("src", "templates").absolute())
    setup_routes(app)
    configure_env(app)
    init_app(app)
    return app
