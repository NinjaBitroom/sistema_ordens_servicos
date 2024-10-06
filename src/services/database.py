"""."""

from flask_sqlalchemy import SQLAlchemy

from src.services.base_model import BaseModel

DB = SQLAlchemy(model_class=BaseModel)
