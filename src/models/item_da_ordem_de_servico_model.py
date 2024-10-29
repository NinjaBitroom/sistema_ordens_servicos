"""."""

from pydantic import NonNegativeFloat, NonNegativeInt
from sqlmodel import (
    Field,  # type: ignore[reportUnknownVariableType]
    Relationship,
)

from src.models.base.base_model import BaseModel
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.models.produto_model import ProdutoModel


class ItemDaOrdemDeServicoModel(BaseModel, table=True):
    """."""

    __tablename__ = "Itens da ordem de serviço"
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    ordem_de_servico_id: NonNegativeInt | None = Field(
        foreign_key="Ordens de serviço.id", nullable=False
    )
    ordem_de_servico: OrdemDeServicoModel | None = Relationship(
        back_populates="itens_da_ordem_de_servico"
    )
    produto_id: NonNegativeInt | None = Field(
        foreign_key="Produtos.id", nullable=False
    )
    produto: ProdutoModel | None = Relationship()
    quantidade: NonNegativeInt
    valor_total_do_item: NonNegativeFloat
