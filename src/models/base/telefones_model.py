"""."""

from sqlalchemy.orm import Mapped

from src.services.database import DB


class TelefonesModel(DB.Model):
    """."""

    __abstract__ = True
    telefone_fixo: Mapped[str | None]
    telefone_celular: Mapped[str | None]
