"""."""

from dataclasses import dataclass

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003


@dataclass
class FormCreateResponse[T: FlaskForm]:
    """."""

    exception: Exception | None
    form: T
