"""."""

from pydantic import NonNegativeInt
from sqlmodel import Field  # type: ignore  # noqa: PGH003

from src.services.database import DB


class CargoDoFuncionarioModel(DB.Model, table=True):
    """."""

    __tablename__ = "Cargos dos funcionários"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
