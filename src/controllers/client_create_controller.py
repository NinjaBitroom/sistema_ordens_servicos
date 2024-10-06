"""."""

from src.forms.cliente_form import ClienteForm
from src.protocols.controller import Controller
from src.protocols.db.db_add_one_operation import DbAddOneOperation
from src.protocols.validaton import Validation


class ClientCreateController(Controller):
    """."""

    def __init__(
        self,
        validation: Validation,
        db_add_one_operation: DbAddOneOperation,
    ) -> None:
        """."""
        self.__VALIDATION = validation
        self.__DB_ADD_ONE_OPERATION = db_add_one_operation

    def handle(self, request: ClienteForm) -> None | Exception:
        """."""
        exception = self.__VALIDATION.validate(request)
        if exception is None:
            self.__DB_ADD_ONE_OPERATION.add_one(request.data)
        return exception
