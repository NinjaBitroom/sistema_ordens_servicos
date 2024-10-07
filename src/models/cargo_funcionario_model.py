"""."""

from sqlalchemy.orm import Mapped, mapped_column

from services.database import DB
from src.services.base_model import BaseModel


class CargoFuncionarioModel(DB.Model, BaseModel):
    """."""

    __tablename__ = "Cargos dos funcionários"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
