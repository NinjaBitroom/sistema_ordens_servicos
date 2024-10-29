"""."""

from datetime import date

from pydantic import EmailStr, NonNegativeInt
from sqlalchemy_utils import (  # pyright: ignore[reportMissingTypeStubs]
    EmailType,
)
from sqlmodel import Field  # pyright: ignore[reportUnknownVariableType]

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel


class EmpresaModel(EnderecoModel, TelefonesModel, table=True):
    """."""

    __tablename__ = "Empresa"
    id: NonNegativeInt | None = Field(
        default=None, primary_key=True, title="ID"
    )
    nome: str = Field(index=True, unique=True, title="Nome")
    cnpj: str = Field(min_length=14, max_length=14, unique=True, title="CNPJ")
    email: EmailStr | None = Field(
        sa_type=EmailType, unique=True, title="E-mail"
    )
    data_de_cadastro_no_sistema: date | None = Field(
        default_factory=date.today, title="Data de cadastro no sistema"
    )

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
