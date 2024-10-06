"""."""

from abc import ABC, abstractmethod


class Controller(ABC):
    """."""

    @abstractmethod
    def handle(self, request: object) -> object:
        """."""
