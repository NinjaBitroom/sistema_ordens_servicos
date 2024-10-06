"""."""

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from models.endereco_model import EnderecoModel
from models.telefones_model import TelefonesModel


class EmpresaModel(EnderecoModel, TelefonesModel):
    """."""

    __tablename__ = "Empresa"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    cnpj: Mapped[str]
    email: Mapped[str | None]
    data_de_cadastro: Mapped[datetime | None] = mapped_column(
        default_factory=datetime.now
    )
