"""."""

from os import environ

from flask import Flask


def configure_env(app: Flask) -> None:
    """."""
    app.config["SQLALCHEMY_ENGINES"] = {
        "default": environ.get("SQL_URI", "sqlite:///db.sqlite3")
    }
    app.config["ALEMBIC"] = {
        "post_write_hooks": {
            "hooks": "ruff, pre-commit, git",
            "ruff.type": "exec",
            "ruff.executable": "ruff",
            "ruff.options": "format REVISION_SCRIPT_FILENAME",
            "pre-commit.type": "exec",
            "pre-commit.executable": "pre-commit",
            "pre-commit.options": "run --files REVISION_SCRIPT_FILENAME",
            "git.type": "exec",
            "git.executable": "git",
            "git.options": "add REVISION_SCRIPT_FILENAME",
        }
    }
    app.config["ALEMBIC_CONTEXT"] = {"user_module_prefix": "sqlmodel."}
    app.secret_key = environ.get("SECRET_KEY", "segredo!")
