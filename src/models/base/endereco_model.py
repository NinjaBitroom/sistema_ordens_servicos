"""."""

from sqlmodel import Field  # pyright: ignore[reportUnknownVariableType]

from src.models.base.base_model import BaseModel


class EnderecoModel(BaseModel):
    """."""

    endereco_rua: str | None = Field(title="Rua")
    endereco_bairro: str | None = Field(title="Bairro")
    endereco_numero: int | None = Field(title="Número do endereço")
    endereco_cep: str | None = Field(min_length=8, max_length=8, title="CEP")
