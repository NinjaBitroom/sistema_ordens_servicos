"""."""

from flask_alembic import Alembic
from sqlmodel import SQLModel

ALEMBIC = Alembic(metadatas=SQLModel.metadata)
