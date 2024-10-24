"""."""

from datetime import date

from pydantic import EmailStr, NonNegativeInt, PastDate
from sqlalchemy import Date
from sqlalchemy_utils import EmailType  # type: ignore  # noqa: PGH003
from sqlmodel import Field  # type: ignore  # noqa: PGH003

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel
from src.protocols.genders import Genders


class ClienteModel(EnderecoModel, TelefonesModel, table=True):
    """."""

    __tablename__ = "Clientes"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True)
    sexo: Genders | None = Field(default=None)
    nascimento: PastDate | None = Field(sa_type=Date)
    cpf: str | None = Field(min_length=11, max_length=14)
    data_de_cadastro: date | None = Field(default_factory=date.today)
    email: EmailStr | None = Field(sa_type=EmailType)

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
