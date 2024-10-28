"""."""

from typing import cast

from pydantic_extra_types.phone_numbers import PhoneNumber
from sqlalchemy_utils import (  # type: ignore[reportMissingTypeStubs]
    PhoneNumberType,
)
from sqlmodel import Field  # type: ignore[reportUnknownVariableType]

from src.models.base.base_model import BaseModel

PhoneNumber.default_region_code = "BR"


class TelefonesModel(BaseModel):
    """."""

    telefone_fixo: PhoneNumber | None = Field(
        sa_type=cast(type, PhoneNumberType(region="BR"))
    )
    telefone_celular: PhoneNumber | None = Field(
        sa_type=cast(type, PhoneNumberType(region="BR"))
    )
