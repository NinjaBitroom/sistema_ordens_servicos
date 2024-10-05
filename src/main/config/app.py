from flask import Flask

from src.services.database import DB


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    DB.init_app(app)
    return app
