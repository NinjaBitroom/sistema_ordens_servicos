from services.database import DB
from sqlalchemy.orm import Mapped


class TelefoneModel(DB.Model):
    __abstract__ = True
    telefone_fixo: Mapped[str | None]
    telefone_celular: Mapped[str | None]
