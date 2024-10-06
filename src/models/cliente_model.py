"""."""

from datetime import date, datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.endereco_model import EnderecoModel
from src.models.telefones_model import TelefonesModel


class ClienteModel(EnderecoModel, TelefonesModel):
    """."""

    __tablename__ = "Clientes"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    sexo: Mapped[str | None] = mapped_column(String(1))
    nascimento: Mapped[date | None]
    cpf: Mapped[str | None]
    data_de_cadastro: Mapped[datetime | None] = mapped_column(
        default_factory=datetime.now
    )
    email: Mapped[str | None] = mapped_column(default=None)
