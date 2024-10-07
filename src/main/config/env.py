"""."""

from os import environ

from flask import Flask


def configure_env(app: Flask) -> None:
    """."""
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get(
        "SQL_URI", "sqlite:///db.sqlite3"
    )
    app.secret_key = environ.get("SECRET_KEY", "segredo!")
