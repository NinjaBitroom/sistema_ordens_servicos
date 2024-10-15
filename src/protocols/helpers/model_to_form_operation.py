"""."""

from abc import ABC, abstractmethod


class ModelToFormOperation[TModel, TForm](ABC):
    """."""

    @abstractmethod
    def model_to_form(self, model: type[TModel]) -> type[TForm]:
        """."""
