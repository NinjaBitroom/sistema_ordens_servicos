"""."""

from datetime import date

from pydantic import EmailStr, NonNegativeInt, PastDate
from sqlalchemy import Date
from sqlalchemy_utils import (  # pyright: ignore[reportMissingTypeStubs]
    EmailType,
)
from sqlmodel import (
    Field,  # pyright: ignore[reportUnknownVariableType]
    Relationship,
)

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel
from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.models.escolaridade_model import EscolaridadeModel
from src.protocols.genders import Genders


class FuncionarioModel(EnderecoModel, TelefonesModel, table=True):
    """."""

    __tablename__ = "Funcionários"
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True)
    sexo: Genders | None = Field(default=None)
    nascimento: PastDate | None = Field(sa_type=Date)
    cpf: str | None = Field(min_length=11, max_length=11, unique=True)
    email: EmailStr | None = Field(sa_type=EmailType)
    cargo_id: NonNegativeInt | None = Field(
        foreign_key="Cargos dos funcionários.id", nullable=False
    )
    cargo: CargoDoFuncionarioModel | None = Relationship()
    data_de_cadastro: date | None = Field(default_factory=date.today)
    escolaridade_id: NonNegativeInt | None = Field(
        foreign_key="Escolaridades.id", nullable=False
    )
    escolaridade: EscolaridadeModel | None = Relationship()

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
