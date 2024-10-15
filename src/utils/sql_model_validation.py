"""."""

from pydantic import ValidationError
from sqlmodel import SQLModel

from src.protocols.validaton import Validation


class SqlModelValidation[T: SQLModel](Validation[T]):
    """."""

    def __init__(self, model_class: type[T]) -> None:
        """."""
        self.__MODEL_CLASS = model_class

    def validate(self, data: T) -> None | Exception:
        """."""
        try:
            self.__MODEL_CLASS.model_validate(data)
        except ValidationError as exception:
            return exception
        else:
            return None
