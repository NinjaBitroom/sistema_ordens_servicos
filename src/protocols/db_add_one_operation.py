"""."""

from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any


class DbAddOneOperation(ABC):
    """."""

    @abstractmethod
    def add_one(self, data: Mapping[Any, Any]) -> None:
        """."""
