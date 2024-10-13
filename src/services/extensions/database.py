"""."""

from sqlmodel import SQLModel

from src.services.protocols.base_session import BaseSession
from src.services.protocols.custom_sql_alchemy import CustomSQLAlchemy

DB = CustomSQLAlchemy(
    model_class=SQLModel, session_options={"class_": BaseSession}
)
