"""."""

from pydantic import NonNegativeInt
from sqlmodel import Field  # type: ignore[reportUnknownVariableType]

from src.models.base.base_model import BaseModel


class MarcaModel(BaseModel, table=True):
    """."""

    __tablename__ = "Marcas"
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True, unique=True)

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
