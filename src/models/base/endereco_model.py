"""."""

from sqlmodel import Field, SQLModel  # type: ignore  # noqa: PGH003


class EnderecoModel(SQLModel):
    """."""

    endereco_rua: str | None
    endereco_bairro: str | None
    endereco_numero: int | None
    endereco_cep: str | None = Field(min_length=8, max_length=9)
