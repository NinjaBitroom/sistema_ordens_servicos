"""."""

from pydantic import NonNegativeFloat, NonNegativeInt
from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
    Relationship,
)

from src.models.base.base_model import BaseModel
from src.models.ordem_de_servico_model import OrdemDeServicoModel


class ContaAReceberModel(BaseModel, table=True):
    """."""

    __tablename__ = "Contas a receber"
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    ordem_de_servico_id: NonNegativeInt | None = Field(
        foreign_key="Ordens de serviço.id"
    )
    ordem_de_servico: OrdemDeServicoModel | None = Relationship()
    valor: NonNegativeFloat
