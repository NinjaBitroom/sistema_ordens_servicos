"""."""

from datetime import date

from pydantic import NonNegativeFloat, NonNegativeInt
from sqlalchemy import Text
from sqlmodel import (
    Field,  # type: ignore[reportUnknownVariableType]
    Relationship,
)

from src.models.base.base_model import BaseModel
from src.models.cliente_model import ClienteModel
from src.models.funcionario_model import FuncionarioModel


class OrdemDeServicoModel(BaseModel, table=True):
    """."""

    __tablename__ = "Ordens de serviço"
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    tecnico_id: NonNegativeInt | None = Field(
        foreign_key="Funcionários.id", nullable=False
    )
    tecnico: FuncionarioModel | None = Relationship()
    cliente_id: NonNegativeInt | None = Field(
        foreign_key="Clientes.id", nullable=False
    )
    cliente: ClienteModel | None = Relationship()
    descricao_do_problema: str = Field(sa_type=Text)
    valor_total_da_ordem: NonNegativeFloat
    data_: date = Field(
        default_factory=date.today, sa_column_kwargs={"name": "data"}
    )
    aberto: bool = Field(default=True)
