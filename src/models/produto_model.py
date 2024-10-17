"""."""

from pydantic import NonNegativeFloat, NonNegativeInt
from sqlmodel import (
    Field,  # type: ignore  # noqa: PGH003
    Relationship,
    SQLModel,
)

from src.models.marca_model import MarcaModel


class ProdutoModel(SQLModel, table=True):
    """."""

    __tablename__ = "Produtos"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str
    valor_venda: NonNegativeFloat
    quantidade_em_estoque: NonNegativeInt
    marca_id: NonNegativeInt | None = Field(
        default=None, foreign_key="Marcas.id"
    )
    marca: MarcaModel | None = Relationship()

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
