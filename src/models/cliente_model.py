"""."""

from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel
from src.protocols.genders import Genders


class ClienteModel(EnderecoModel, TelefonesModel):
    """."""

    __tablename__ = "Clientes"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    sexo: Mapped[Genders | None] = mapped_column()
    nascimento: Mapped[date | None]
    cpf: Mapped[str | None]
    data_de_cadastro: Mapped[date | None] = mapped_column(
        default_factory=date.today
    )
    email: Mapped[str | None] = mapped_column(default=None)

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
