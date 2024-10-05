from services.database import DB
from sqlalchemy.orm import Mapped


class EnderecoModel(DB.Model):
    __abstract__ = True
    endereco_rua: Mapped[str | None]
    endereco_bairro: Mapped[str | None]
    endereco_numero: Mapped[int | None]
    endereco_cep: Mapped[str | None]
