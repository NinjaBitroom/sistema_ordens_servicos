"""."""

from sqlalchemy.orm import Mapped, mapped_column

from services.database import DB
from src.services.base_model import BaseModel


class EscolaridadeModel(DB.Model, BaseModel):
    """."""

    __tablename__ = "Escolaridades"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
