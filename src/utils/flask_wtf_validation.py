"""."""

from flask_wtf import FlaskForm

from src.protocols.validaton import Validation


class FlaskWtfValidation(Validation):
    """."""

    def validate(self, data: FlaskForm) -> None | Exception:
        """."""
        if data.validate_on_submit():
            return None
        errors_list = list[str]()
        for field, errors in data.errors.items():
            for error in errors:
                errors_list.append(f"{field}: {error}")
        return Exception(*errors_list)
