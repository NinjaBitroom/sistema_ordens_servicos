"""."""

from decimal import Decimal

from pydantic import NonNegativeInt
from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
    Relationship,
)

from src.models.base.base_model import BaseModel
from src.models.marca_model import MarcaModel


class ProdutoModel(BaseModel, table=True):
    """."""

    __tablename__ = "Produtos"
    id: NonNegativeInt | None = Field(
        default=None, primary_key=True, title="ID"
    )
    nome: str = Field(index=True, unique=True, title="Nome")
    valor_venda: Decimal = Field(
        title="Valor de venda", decimal_places=2, ge=0
    )
    quantidade_em_estoque: NonNegativeInt = Field(
        title="Quantidade em estoque"
    )
    marca_id: NonNegativeInt | None = Field(
        default=None,
        foreign_key="Marcas.id",
        nullable=False,
        title="ID da marca",
    )
    marca: MarcaModel | None = Relationship()

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
