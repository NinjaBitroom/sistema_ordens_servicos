"""."""

from abc import ABC, abstractmethod


class FlaskWtfController(ABC):
    """."""

    @abstractmethod
    def validate(self) -> object:
        """."""
