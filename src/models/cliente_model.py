"""."""

from datetime import date

from pydantic import EmailStr, NonNegativeInt, PastDate
from sqlalchemy import Date
from sqlalchemy_utils import (  # pyright: ignore[reportMissingTypeStubs]
    EmailType,
)
from sqlmodel import Field  # pyright: ignore[reportUnknownVariableType]

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel
from src.protocols.genders import Genders


class ClienteModel(EnderecoModel, TelefonesModel, table=True):
    """."""

    __tablename__ = "Clientes"
    id: NonNegativeInt | None = Field(
        default=None, primary_key=True, title="ID"
    )
    nome: str = Field(index=True, title="Nome")
    sexo: Genders | None = Field(default=None, title="Gênero")
    nascimento: PastDate | None = Field(
        sa_type=Date, title="Data de nascimento"
    )
    cpf: str | None = Field(
        min_length=11, max_length=11, unique=True, title="CPF"
    )
    data_de_cadastro: date | None = Field(
        default_factory=date.today, title="Data de cadastro"
    )
    email: EmailStr | None = Field(
        sa_type=EmailType, unique=True, title="E-mail"
    )

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
