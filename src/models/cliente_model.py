from datetime import date, datetime

from sqlalchemy import String
from models.endereco_model import EnderecoModel
from sqlalchemy.orm import Mapped, mapped_column

from models.telefones_model import TelefoneModel


class ClienteModel(EnderecoModel, TelefoneModel):
    __tablename__ = 'Clientes'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    sexo: Mapped[str | None] = mapped_column(String(1))
    nascimento: Mapped[date | None]
    cpf: Mapped[str | None]
    data_de_cadastro: Mapped[datetime | None] = mapped_column(default_factory=datetime.now)
    email: Mapped[str | None]
