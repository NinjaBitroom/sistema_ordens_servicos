"""."""

from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel


class EmpresaModel(EnderecoModel, TelefonesModel):
    """."""

    __tablename__ = "Empresa"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    cnpj: Mapped[str]
    email: Mapped[str | None]
    data_de_cadastro_no_sistema: Mapped[date | None] = mapped_column(
        default_factory=date.today
    )

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
