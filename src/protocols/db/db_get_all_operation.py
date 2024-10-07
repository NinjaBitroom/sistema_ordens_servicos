"""."""

from abc import ABC, abstractmethod
from collections.abc import Sequence


class DbGetAllOperation[T](ABC):
    """."""

    @abstractmethod
    def get_all(self) -> Sequence[T]:
        """."""
