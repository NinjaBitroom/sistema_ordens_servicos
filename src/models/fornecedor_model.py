"""."""

from datetime import date

from pydantic import EmailStr, NonNegativeInt
from sqlalchemy_utils import (  # pyright: ignore[reportMissingTypeStubs]
    EmailType,
)
from sqlmodel import Field  # pyright: ignore[reportUnknownVariableType]

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel


class FornecedorModel(EnderecoModel, TelefonesModel, table=True):
    """."""

    __tablename__ = "Fornecedores"
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str = Field(index=True, unique=True)
    cnpj: str = Field(min_length=14, max_length=14, unique=True)
    email: EmailStr | None = Field(sa_type=EmailType, unique=True)
    data_de_cadastro_no_sistema: date | None = Field(
        default_factory=date.today
    )

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
