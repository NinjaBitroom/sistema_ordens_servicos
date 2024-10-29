"""."""

from flask_wtf import FlaskForm  # pyright: ignore[reportMissingTypeStubs]

from src.protocols.validaton import Validation


class FlaskWtfValidation(Validation[FlaskForm]):
    """."""

    def validate(self, data: FlaskForm) -> None | Exception:
        """."""
        if data.validate_on_submit():  # pyright: ignore[reportUnknownMemberType]
            return None
        errors_list = list[str]()
        for field, errors in data.errors.items():
            for error in errors:
                errors_list.append(f"{field}: {error}")
        return Exception(*errors_list)
