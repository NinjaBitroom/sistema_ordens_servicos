"""."""

from datetime import date

from pydantic import EmailStr, NonNegativeInt
from sqlalchemy_utils import EmailType  # type: ignore  # noqa: PGH003
from sqlmodel import Field  # type: ignore  # noqa: PGH003

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel


class EmpresaModel(EnderecoModel, TelefonesModel, table=True):
    """."""

    __tablename__ = "Empresa"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str
    cnpj: str
    email: EmailStr | None = Field(sa_type=EmailType)
    data_de_cadastro_no_sistema: date | None = Field(
        default_factory=date.today
    )

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
