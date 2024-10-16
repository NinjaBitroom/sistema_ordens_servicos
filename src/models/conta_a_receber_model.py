"""."""

from pydantic import NonNegativeFloat, NonNegativeInt
from sqlmodel import (
    Field,  # type: ignore  # noqa: PGH003
    Relationship,
    SQLModel,
)

from src.models.ordem_de_servico_model import OrdemDeServicoModel


class ContaAReceberModel(SQLModel, table=True):
    """."""

    __tablename__ = "Contas a receber"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    ordem_de_servico_id: NonNegativeInt | None = Field(
        foreign_key="Ordens de serviço.id"
    )
    ordem_de_servico: OrdemDeServicoModel | None = Relationship()
    valor: NonNegativeFloat
