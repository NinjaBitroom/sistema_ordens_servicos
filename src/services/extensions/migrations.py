"""."""

from flask_alembic import Alembic

from src.models.base.base_model import BaseModel

ALEMBIC = Alembic(metadatas=BaseModel.metadata)
