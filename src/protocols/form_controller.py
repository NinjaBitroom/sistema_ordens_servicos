"""."""

from abc import ABC, abstractmethod


class FormController(ABC):
    """."""

    @abstractmethod
    def validate(self) -> object:
        """."""
