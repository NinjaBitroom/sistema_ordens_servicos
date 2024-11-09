"""."""

from decimal import Decimal

from pydantic import NonNegativeInt
from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
)

from src.models.base.base_model import BaseModel


class ItemDaOrdemDeServicoModel(BaseModel, table=True):
    """."""

    __tablename__ = "Itens da ordem de serviço"
    id: NonNegativeInt | None = Field(
        default=None, primary_key=True, title="ID"
    )
    ordem_de_servico_id: NonNegativeInt | None = Field(
        foreign_key="Ordens de serviço.id",
        nullable=False,
        title="ID da ordem de serviço",
    )
    produto_id: NonNegativeInt | None = Field(
        foreign_key="Produtos.id", nullable=False, title="ID do produto"
    )
    quantidade: NonNegativeInt = Field(title="Quantidade", default=1)
    valor_total_do_item: Decimal = Field(
        title="Valor total do item", decimal_places=2, ge=0, default=0
    )
