"""."""

from datetime import date

from pydantic import NonNegativeFloat, NonNegativeInt
from sqlalchemy import Text
from sqlmodel import (
    Field,  # type: ignore  # noqa: PGH003
    Relationship,
    SQLModel,
)

from src.models.cliente_model import ClienteModel
from src.models.funcionario_model import FuncionarioModel


class OrdemDeServicoModel(SQLModel, table=True):
    """."""

    __tablename__ = "Ordens de serviço"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    tecnico_id: NonNegativeInt | None = Field(foreign_key="Funcionários.id")
    tecnico: FuncionarioModel | None = Relationship()
    cliente_id: NonNegativeInt | None = Field(foreign_key="Clientes.id")
    cliente: ClienteModel | None = Relationship()
    descricao_do_problema: str = Field(sa_type=Text)
    valor_total_da_ordem: NonNegativeFloat
    data_: date = Field(default_factory=date.today)
    aberto: bool = Field(default=True)
