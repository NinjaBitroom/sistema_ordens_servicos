"""."""

from datetime import date

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

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
    cargo: Mapped[CargoDoFuncionarioModel] = relationship(default=None)
    data_de_cadastro: Mapped[date | None] = mapped_column(
        default_factory=date.today
    )
