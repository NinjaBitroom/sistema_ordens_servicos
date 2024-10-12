"""."""

from src.services.database import DB


class EnderecoModel(DB.Model):
    """."""

    endereco_rua: str | None
    endereco_bairro: str | None
    endereco_numero: int | None
    endereco_cep: str | None
