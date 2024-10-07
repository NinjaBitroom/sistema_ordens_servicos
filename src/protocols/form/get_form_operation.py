"""."""

from abc import ABC, abstractmethod


class GetFormOperation[TIn, TOut](ABC):
    """."""

    @abstractmethod
    def get_form(self, from_: TIn) -> TOut:
        """."""
