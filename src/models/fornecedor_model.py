from datetime import datetime
from models.endereco_model import EnderecoModel
from models.telefones_model import TelefoneModel
from sqlalchemy.orm import Mapped, mapped_column


class FornecedorModel(EnderecoModel, TelefoneModel):
    __tablename__ = 'Fornecedores'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    cnpj: Mapped[str]
    email: Mapped[str | None]
    data_de_cadastro: Mapped[datetime | None] = mapped_column(default_factory=datetime.now)
