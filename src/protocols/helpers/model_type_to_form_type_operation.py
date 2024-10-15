"""."""

from abc import ABC, abstractmethod


class ModelTypeToFormTypeOperation[TModel, TForm](ABC):
    """."""

    @abstractmethod
    def model_type_to_form_type(
        self, model_class: type[TModel]
    ) -> type[TForm]:
        """."""
