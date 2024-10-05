from pathlib import Path

from flask import Flask

from src.main.config.db import create_tables
from src.main.config.routes import setup_routes
from src.services.database import DB


def create_app() -> Flask:
    app = Flask(__name__, template_folder=Path("src", "templates").absolute())
    setup_routes(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.secret_key = "secret"
    DB.init_app(app)
    create_tables(app, DB)
    return app
