"""."""

from sqlmodel import SQLModel


class EnderecoModel(SQLModel):
    """."""

    endereco_rua: str | None
    endereco_bairro: str | None
    endereco_numero: int | None
    endereco_cep: str | None
