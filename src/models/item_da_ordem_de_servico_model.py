"""."""

from pydantic import NonNegativeInt
from sqlmodel import (
    Field,  # type: ignore  # noqa: PGH003
    Relationship,
)

from models.produto_model import ProdutoModel
from services.database import DB


class ItemDaOrdemDeServicoModel(DB.Model, table=True):
    """."""

    __tablename__ = "Itens da ordem de serviço"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    produto_id: NonNegativeInt | None = Field(foreign_key=ProdutoModel.id)
    produto: ProdutoModel | None = Relationship()
    quantidade: NonNegativeInt
    valor_total_do_item: float
