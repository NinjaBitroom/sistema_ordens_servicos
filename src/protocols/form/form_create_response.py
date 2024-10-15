"""."""

from dataclasses import dataclass


@dataclass
class FormCreateResponse[T]:
    """."""

    exception: Exception | None
    form: T
