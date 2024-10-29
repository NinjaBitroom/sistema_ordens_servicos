"""."""

from collections.abc import Mapping
from typing import Any

from wtforms import EmailField, StringField, TelField
from wtforms_sqlalchemy.orm import (  # pyright: ignore[reportMissingTypeStubs]
    ModelConverter,
    converts,  # pyright: ignore[reportUnknownVariableType]
)


class SqlModelConverter(ModelConverter):
    """."""

    @converts("sqlmodel.sql.sqltypes.AutoString")
    def conv_auto_string(
        self, field_args: Mapping[Any, Any], **extra: object
    ) -> StringField:
        """."""
        return self.conv_String(field_args, **extra)  # pyright: ignore[reportUnknownMemberType]

    @converts("sqlalchemy_utils.types.phone_number.PhoneNumberType")
    def conv_phone_number(
        self, field_args: Mapping[Any, Any], **extra: object
    ) -> TelField:
        """."""
        self._string_common(field_args=field_args, **extra)  # pyright: ignore[reportUnknownMemberType]
        return TelField(**field_args)

    @converts("sqlalchemy_utils.types.email.EmailType")
    def conv_email(
        self, field_args: Mapping[Any, Any], **extra: object
    ) -> EmailField:
        """."""
        self._string_common(field_args=field_args, **extra)  # pyright: ignore[reportUnknownMemberType]
        return EmailField(**field_args)
