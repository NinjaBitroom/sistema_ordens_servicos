"""."""

from datetime import date

from pydantic import EmailStr, NonNegativeInt, PastDate
from sqlalchemy import Date
from sqlalchemy_utils import EmailType  # type: ignore  # noqa: PGH003
from sqlmodel import Field, Relationship  # type: ignore  # noqa: PGH003

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel
from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.models.escolaridade_model import EscolaridadeModel
from src.protocols.genders import Genders


class FuncionarioModel(EnderecoModel, TelefonesModel, table=True):
    """."""

    __tablename__ = "Funcionários"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str
    sexo: Genders | None = Field(default=None)
    nascimento: PastDate | None = Field(sa_type=Date)
    cpf: str | None
    email: EmailStr | None = Field(sa_type=EmailType)
    cargo_id: NonNegativeInt | None = Field(
        foreign_key="Cargos dos funcionários.id"
    )
    cargo: CargoDoFuncionarioModel | None = Relationship()
    data_de_cadastro: date | None = Field(default_factory=date.today)
    escolaridade_id: NonNegativeInt | None = Field(
        foreign_key="Escolaridades.id"
    )
    escolaridade: EscolaridadeModel | None = Relationship()

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
