"""."""

from abc import ABC, abstractmethod

from src.protocols.db.update_data import UpdateData


class DbUpdateOperation[T](ABC):
    """."""

    @abstractmethod
    def update(self, data: UpdateData[T]) -> None:
        """."""
