"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.protocols.validaton import Validation


class FlaskWtfValidation[T: FlaskForm](Validation[T]):
    """."""

    def validate(self, data: T) -> None | Exception:
        """."""
        if data.validate_on_submit():  # type: ignore  # noqa: PGH003
            return None
        errors_list = list[str]()
        for field, errors in data.errors.items():
            for error in errors:
                errors_list.append(f"{field}: {error}")
        return Exception(*errors_list)
