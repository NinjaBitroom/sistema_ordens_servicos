"""."""

from pydantic import NonNegativeFloat, NonNegativeInt
from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
    Relationship,
)

from src.models.base.base_model import BaseModel
from src.models.marca_model import MarcaModel


class ProdutoModel(BaseModel, table=True):
    """."""

    __tablename__ = "Produtos"
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True)
    valor_venda: NonNegativeFloat
    quantidade_em_estoque: NonNegativeInt
    marca_id: NonNegativeInt | None = Field(
        default=None, foreign_key="Marcas.id", nullable=False
    )
    marca: MarcaModel | None = Relationship()

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
