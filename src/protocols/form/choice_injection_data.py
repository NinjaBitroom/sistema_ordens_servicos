"""."""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class ChoiceInjectionData[TChoices, TForm]:
    """."""

    choices: Iterable[TChoices]
    field_name: str
    form: TForm
