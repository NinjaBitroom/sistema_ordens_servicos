"""."""

from pydantic import NonNegativeFloat, NonNegativeInt
from sqlmodel import (
    Field,  # type: ignore  # noqa: PGH003
    Relationship,
    SQLModel,
)

from src.models.produto_model import ProdutoModel


class ItemDaOrdemDeServicoModel(SQLModel, table=True):
    """."""

    __tablename__ = "Itens da ordem de serviço"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    produto_id: NonNegativeInt | None = Field(foreign_key="Produtos.id")
    produto: ProdutoModel | None = Relationship()
    quantidade: NonNegativeInt
    valor_total_do_item: NonNegativeFloat
