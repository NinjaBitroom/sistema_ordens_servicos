from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_tables(app: Flask, db: SQLAlchemy) -> None:
    with app.app_context():
        db.create_all()
