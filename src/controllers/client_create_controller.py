"""."""

from src.forms.cliente_form import ClienteForm
from src.protocols.controller import Controller
from src.protocols.db_add_one_operation import DbAddOneOperation
from src.protocols.validaton import Validation


class ClientCreateController(Controller):
    """."""

    def __init__(
        self,
        validation: Validation,
        db_add_one_operation: DbAddOneOperation,
    ) -> None:
        """."""
        self.validation = validation
        self.db_add_one_operation = db_add_one_operation

    def handle(self, request: ClienteForm) -> None | Exception:
        """."""
        exception = self.validation.validate(request)
        if exception is None:
            self.db_add_one_operation.add_one(request.data)
        return exception
