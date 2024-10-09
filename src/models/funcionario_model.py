"""."""

from datetime import date, datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel
from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel


class FuncionarioModel(EnderecoModel, TelefonesModel):
    """."""

    __tablename__ = "Funcionários"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    sexo: Mapped[str | None] = mapped_column(String(1))
    nascimento: Mapped[date | None]
    cpf: Mapped[str | None]
    email: Mapped[str | None]
    cargo_id: Mapped[int] = mapped_column(
        ForeignKey(CargoDoFuncionarioModel.id)
    )
    data_de_cadastro: Mapped[datetime | None] = mapped_column(
        default_factory=datetime.now
    )
