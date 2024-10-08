"""."""

from abc import ABC, abstractmethod

from src.protocols.form.choice_injection_data import ChoiceInjectionData


class InjectChoicesOperation[TChoices, TForm](ABC):
    """."""

    @abstractmethod
    def inject_choices(
        self, data: ChoiceInjectionData[TChoices, TForm]
    ) -> None:
        """."""
