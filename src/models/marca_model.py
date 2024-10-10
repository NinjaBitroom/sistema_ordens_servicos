"""."""

from sqlalchemy.orm import Mapped, mapped_column

from services.database import DB
from src.services.base_model import BaseModel


class MarcaModel(DB.Model, BaseModel):
    """."""

    __tablename__ = "Marcas"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
