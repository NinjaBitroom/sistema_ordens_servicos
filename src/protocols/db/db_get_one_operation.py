"""."""

from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any


class DbGetOneOperation[T](ABC):
    """."""

    @abstractmethod
    def get_one(self, data: Mapping[Any, Any]) -> T:
        """."""
