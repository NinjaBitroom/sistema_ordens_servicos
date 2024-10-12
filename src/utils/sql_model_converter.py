"""."""

from wtforms import StringField
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
        return self.conv_String(field_args, **extra)  # type: ignore  # noqa: PGH003
