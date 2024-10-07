"""."""

from dataclasses import dataclass

from src.forms.cliente_form import ClienteForm


@dataclass
class ClientCreateResponse:
    """."""

    exception: Exception | None
    form: ClienteForm
