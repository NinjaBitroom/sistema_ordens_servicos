"""."""

from datetime import date

from pydantic import EmailStr, NonNegativeInt, PastDate
from sqlalchemy import Date
from sqlmodel import Field  # type: ignore  # noqa: PGH003

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel
from src.protocols.genders import Genders


class ClienteModel(EnderecoModel, TelefonesModel, table=True):
    """."""

    __tablename__ = "Clientes"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str
    sexo: Genders | None = Field()
    nascimento: PastDate | None = Field(sa_type=Date)
    cpf: str | None
    data_de_cadastro: date | None = Field(default_factory=date.today)
    email: EmailStr | None = Field(default=None)

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
