"""."""

from abc import ABC, abstractmethod


class Validation[T](ABC):
    """."""

    @abstractmethod
    def validate(self, data: T) -> None | Exception:
        """."""
