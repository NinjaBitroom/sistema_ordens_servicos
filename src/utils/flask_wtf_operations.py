"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.protocols.form.get_form_operation import GetFormOperation


class FlaskWtfOperations[T: FlaskForm](GetFormOperation[type[T], T]):
    """."""

    def get_form(self, from_: type[T]) -> T:
        """."""
        return from_()
