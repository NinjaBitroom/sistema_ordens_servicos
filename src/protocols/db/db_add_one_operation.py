"""."""

from abc import ABC, abstractmethod


class DbAddOneOperation[T](ABC):
    """."""

    @abstractmethod
    def add_one(self, data: T) -> None:
        """."""
