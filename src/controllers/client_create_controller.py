"""."""

from src.forms.client_form import ClientForm
from src.protocols.flask_wtf_controller import FlaskWtfController


class ClientCreateController(FlaskWtfController):
    """."""

    def __init__(self, form: ClientForm) -> None:
        """."""
        self.form = form

    def validate(self) -> None | Exception:
        """."""
        if self.form.validate_on_submit():
            return None
        errors_list = list[str]()
        for field, errors in self.form.errors.items():
            for error in errors:
                errors_list.append(f"{field}: {error}")
        return Exception(*errors_list)
