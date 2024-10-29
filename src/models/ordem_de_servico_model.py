"""."""

from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from pydantic import NonNegativeInt
from sqlalchemy import Text
from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
    Relationship,
)

from src.models.base.base_model import BaseModel
from src.models.cliente_model import ClienteModel
from src.models.funcionario_model import FuncionarioModel

if TYPE_CHECKING:
    from src.models.item_da_ordem_de_servico_model import (
        ItemDaOrdemDeServicoModel,
    )


class OrdemDeServicoModel(BaseModel, table=True):
    """."""

    __tablename__ = "Ordens de serviço"
    id: NonNegativeInt | None = Field(
        default=None, primary_key=True, title="ID"
    )
    itens_da_ordem_de_servico: list["ItemDaOrdemDeServicoModel"] = (
        Relationship(back_populates="ordem_de_servico")
    )
    tecnico_id: NonNegativeInt | None = Field(
        foreign_key="Funcionários.id", nullable=False, title="ID do técnico"
    )
    tecnico: FuncionarioModel | None = Relationship()
    cliente_id: NonNegativeInt | None = Field(
        foreign_key="Clientes.id", nullable=False, title="ID do cliente"
    )
    cliente: ClienteModel | None = Relationship()
    descricao_do_problema: str = Field(
        sa_type=Text, title="Descrição do problema"
    )
    valor_total_da_ordem: Decimal = Field(
        decimal_places=2, title="Valor total da ordem", ge=0
    )
    data_: date = Field(
        default_factory=date.today,
        sa_column_kwargs={"name": "data"},
        title="Data",
    )
    aberto: bool = Field(default=True, title="Aberto")
