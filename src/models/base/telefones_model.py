"""."""

from typing import cast

from pydantic_extra_types.phone_numbers import PhoneNumber
from sqlalchemy_utils import PhoneNumberType  # type: ignore  # noqa: PGH003
from sqlmodel import Field, SQLModel  # type: ignore  # noqa: PGH003

PhoneNumber.default_region_code = "BR"


class TelefonesModel(SQLModel):
    """."""

    telefone_fixo: PhoneNumber | None = Field(
        sa_type=cast(type, PhoneNumberType(region="BR"))
    )
    telefone_celular: PhoneNumber | None = Field(
        sa_type=cast(type, PhoneNumberType(region="BR"))
    )
