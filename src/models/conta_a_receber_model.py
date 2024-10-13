"""."""

from pydantic import NonNegativeInt
from sqlmodel import (
    Field,  # type: ignore  # noqa: PGH003
    Relationship,
)

from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.extensions.database import DB


class ContaAReceberModel(DB.Model, table=True):
    """."""

    __tablename__ = "Contas a receber"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    ordem_de_servico_id: NonNegativeInt | None = Field(
        foreign_key=OrdemDeServicoModel.id
    )
    ordem_de_servico: OrdemDeServicoModel | None = Relationship()
    valor: float
