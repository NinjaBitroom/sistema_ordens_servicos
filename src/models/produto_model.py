"""."""

from pydantic import NonNegativeInt
from sqlmodel import (
    Field,  # type: ignore  # noqa: PGH003
    Relationship,
)

from models.marca_model import MarcaModel
from src.services.extensions.database import DB


class ProdutoModel(DB.Model, table=True):
    """."""

    __tablename__ = "Produtos"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str
    valor_venda: float
    quantidade_em_estoque: NonNegativeInt
    marca_id: NonNegativeInt | None = Field(
        default=None, foreign_key=MarcaModel.id
    )
    marca: MarcaModel | None = Relationship()

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
