"""."""

from pydantic_extra_types.phone_numbers import PhoneNumber

from src.services.extensions.database import DB


class TelefonesModel(DB.Model):
    """."""

    telefone_fixo: PhoneNumber | None
    telefone_celular: PhoneNumber | None
