"""."""

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any


class DbGetAllOperation(ABC):
    """."""

    @abstractmethod
    def get_all(self) -> Sequence[Any]:
        """."""
