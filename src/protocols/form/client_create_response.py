"""."""

from dataclasses import dataclass

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003


@dataclass
class ClientCreateResponse:
    """."""

    exception: Exception | None
    form: FlaskForm
