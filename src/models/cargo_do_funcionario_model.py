"""."""

from sqlalchemy.orm import Mapped, mapped_column

from src.services.base_model import BaseModel
from src.services.database import DB


class CargoDoFuncionarioModel(DB.Model, BaseModel):
    """."""

    __tablename__ = "Cargos dos funcionários"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
