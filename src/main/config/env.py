"""."""

from os import environ

from flask import Flask


def configure_env(app: Flask) -> None:
    """."""
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get(
        "SQL_URI", "sqlite:///db.sqlite3"
    )
    app.config["ALEMBIC"] = {
        "post_write_hooks": {
            "hooks": "ruff",
            "ruff.type": "exec",
            "ruff.entrypoint": "ruff",
            "ruff.executable": "ruff",
            "ruff.options": "format REVISION_SCRIPT_FILENAME",
        }
    }
    app.config["ALEMBIC_CONTEXT"] = {"user_module_prefix": "sqlmodel."}
    app.secret_key = environ.get("SECRET_KEY", "segredo!")
