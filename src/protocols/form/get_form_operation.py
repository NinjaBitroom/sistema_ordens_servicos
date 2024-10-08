"""."""

from abc import ABC, abstractmethod


class GetFormOperation[T](ABC):
    """."""

    @abstractmethod
    def get_form(self) -> T:
        """."""
