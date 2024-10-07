"""."""

from sqlalchemy.orm import Mapped

from src.services.base_model import BaseModel
from src.services.database import DB


class TelefonesModel(DB.Model, BaseModel):
    """."""

    __abstract__ = True
    telefone_fixo: Mapped[str | None]
    telefone_celular: Mapped[str | None]
