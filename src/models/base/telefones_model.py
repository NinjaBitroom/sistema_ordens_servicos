"""."""

from pydantic_extra_types.phone_numbers import PhoneNumber
from sqlalchemy_utils import PhoneNumberType  # type: ignore  # noqa: PGH003
from sqlmodel import Field  # type: ignore  # noqa: PGH003

from src.services.extensions.database import DB


class TelefonesModel(DB.Model):
    """."""

    telefone_fixo: PhoneNumber | None = Field(sa_type=PhoneNumberType)
    telefone_celular: PhoneNumber | None = Field(sa_type=PhoneNumberType)
