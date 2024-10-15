"""."""

from http import HTTPStatus

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.forms.funcionario_model_form import FuncionarioModelForm
from src.protocols.controller import Controller
from src.protocols.db.db_add_one_operation import DbAddOneOperation
from src.protocols.form.form_create_response import FormCreateResponse
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse
from src.protocols.validaton import Validation


class EmployeeCreateController(
    Controller[FlaskForm, FormCreateResponse[FuncionarioModelForm]]
):
    """."""

    def __init__(
        self,
        validation: Validation[FlaskForm],
        db_add_one_operation: DbAddOneOperation,
    ) -> None:
        """."""
        self.__VALIDATION = validation
        self.__DB_ADD_ONE_OPERATION = db_add_one_operation

    def handle(
        self, request: HttpRequest[FlaskForm]
    ) -> HttpResponse[FormCreateResponse[FlaskForm]]:
        """."""
        exception = None
        if request.method == "POST":
            exception = self.__VALIDATION.validate(request.body)
            if exception is None:
                self.__DB_ADD_ONE_OPERATION.add_one(request.body.data)
        response = FormCreateResponse(form=request.body, exception=exception)
        return HttpResponse(body=response, status_code=HTTPStatus.OK)
