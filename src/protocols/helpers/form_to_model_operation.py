"""."""

from abc import ABC, abstractmethod


class FormToModelOperation[TForm, TModel](ABC):
    """."""

    @abstractmethod
    def form_to_model(self, form: TForm) -> TModel:
        """."""
