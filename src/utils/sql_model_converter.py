"""."""

from collections.abc import Mapping
from typing import Any

from wtforms import StringField, TelField
from wtforms_sqlalchemy.orm import (  # type: ignore  # noqa: PGH003
    ModelConverter,
    converts,  # type: ignore  # noqa: PGH003
)


class SqlModelConverter(ModelConverter):
    """."""

    @converts("sqlmodel.sql.sqltypes.AutoString")
    def conv_auto_string(
        self, field_args: object, **extra: object
    ) -> StringField:
        """."""
        StringField()
        return self.conv_String(field_args, **extra)  # type: ignore  # noqa: PGH003

    @converts("sqlalchemy_utils.types.phone_number.PhoneNumberType")
    def conv_phone_number(
        self, field_args: Mapping[Any, Any], **extra: object
    ) -> TelField:
        """."""
        self._string_common(field_args=field_args, **extra)  # type: ignore  # noqa: PGH003
        return TelField(**field_args)
