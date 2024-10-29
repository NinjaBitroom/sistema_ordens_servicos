"""."""

from sqlmodel import Field  # pyright: ignore[reportUnknownVariableType]

from src.models.base.base_model import BaseModel


class EnderecoModel(BaseModel):
    """."""

    endereco_rua: str | None
    endereco_bairro: str | None
    endereco_numero: int | None
    endereco_cep: str | None = Field(min_length=8, max_length=8)
