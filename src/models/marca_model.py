"""."""

from pydantic import NonNegativeInt
from sqlmodel import Field, SQLModel  # type: ignore  # noqa: PGH003


class MarcaModel(SQLModel, table=True):
    """."""

    __tablename__ = "Marcas"  # type: ignore  # noqa: PGH003
    id: NonNegativeInt | None = Field(default=None, primary_key=True)
    nome: str

    def __repr__(self) -> str:
        """."""
        return self.nome

    def __str__(self) -> str:
        """."""
        return self.nome
