"""."""

from abc import ABC, abstractmethod


class DbDeleteOperation[T](ABC):
    """."""

    @abstractmethod
    def delete(self, data: T) -> None:
        """."""
