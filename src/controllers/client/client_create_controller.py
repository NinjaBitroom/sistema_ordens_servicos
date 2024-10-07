"""."""

from http import HTTPStatus

from src.forms.cliente_form import ClienteForm
from src.protocols.controller import Controller
from src.protocols.db.db_add_one_operation import DbAddOneOperation
from src.protocols.form.client_create_response import ClientCreateResponse
from src.protocols.form.get_form_operation import GetFormOperation
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse
from src.protocols.validaton import Validation


class ClientCreateController(Controller[None, ClientCreateResponse]):
    """."""

    def __init__(
        self,
        validation: Validation[ClienteForm],
        db_add_one_operation: DbAddOneOperation,
        get_form_operation: GetFormOperation[type[ClienteForm], ClienteForm],
    ) -> None:
        """."""
        self.__VALIDATION = validation
        self.__DB_ADD_ONE_OPERATION = db_add_one_operation
        self.__GET_FORM_OPERATION = get_form_operation

    def handle(
        self, request: HttpRequest[None]
    ) -> HttpResponse[ClientCreateResponse]:
        """."""
        exception = None
        form = self.__GET_FORM_OPERATION.get_form(ClienteForm)
        if request.method == "POST":
            exception = self.__VALIDATION.validate(form)
            if exception is None:
                self.__DB_ADD_ONE_OPERATION.add_one(form.data)
        response = ClientCreateResponse(form=form, exception=exception)
        return HttpResponse(body=response, status_code=HTTPStatus.OK)
