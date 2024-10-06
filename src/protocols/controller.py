"""."""

from abc import ABC, abstractmethod


class Controller[TReq, TRes](ABC):
    """."""

    @abstractmethod
    def handle(self, request: TReq) -> TRes:
        """."""
