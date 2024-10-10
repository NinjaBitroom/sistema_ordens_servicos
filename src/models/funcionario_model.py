"""."""

from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base.endereco_model import EnderecoModel
from src.models.base.telefones_model import TelefonesModel
from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.protocols.genders import Genders


class FuncionarioModel(EnderecoModel, TelefonesModel):
    """."""

    __tablename__ = "Funcionários"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    sexo: Mapped[Genders | None] = mapped_column()
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

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
