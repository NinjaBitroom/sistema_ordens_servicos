"""."""

from typing import Any

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.protocols.form.choice_injection_data import ChoiceInjectionData
from src.protocols.form.get_form_operation import GetFormOperation
from src.protocols.form.inject_choices_operation import InjectChoicesOperation


class FlaskWtfOperations[T: FlaskForm](
    GetFormOperation[T], InjectChoicesOperation[tuple[Any, Any], T]
):
    """."""

    def __init__(self, form_class: type[T]) -> None:
        """."""
        self.FORM_CLASS = form_class

    def get_form(self) -> T:
        """."""
        return self.FORM_CLASS()

    def inject_choices(
        self, data: ChoiceInjectionData[tuple[str, str], T]
    ) -> None:
        """."""
        getattr(data.form, data.field_name).choices = data.choices
