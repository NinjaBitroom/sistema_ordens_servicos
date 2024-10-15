"""."""

from http import HTTPStatus

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.models.funcionario_model import FuncionarioModel
from src.protocols.controller import Controller
from src.protocols.db.db_add_one_operation import DbAddOneOperation
from src.protocols.form.form_create_response import FormCreateResponse
from src.protocols.helpers.form_to_model_operation import FormToModelOperation
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse
from src.protocols.validaton import Validation


class EmployeeCreateController(
    Controller[FlaskForm, FormCreateResponse[FlaskForm]]
):
    """."""

    def __init__(
        self,
        validation: Validation[FlaskForm],
        db_add_one_operation: DbAddOneOperation[FuncionarioModel],
        form_to_model_operation: FormToModelOperation[
            FlaskForm, FuncionarioModel
        ],
    ) -> None:
        """."""
        self.__VALIDATION = validation
        self.__DB_ADD_ONE_OPERATION = db_add_one_operation
        self.__FORM_TO_MODEL_OPERATION = form_to_model_operation

    def handle(
        self, request: HttpRequest[FlaskForm]
    ) -> HttpResponse[FormCreateResponse[FlaskForm]]:
        """."""
        exception = None
        if request.method == "POST":
            exception = self.__VALIDATION.validate(request.body)
            if exception is None:
                model = self.__FORM_TO_MODEL_OPERATION.form_to_model(
                    request.body
                )
                self.__DB_ADD_ONE_OPERATION.add_one(model)
        response = FormCreateResponse(form=request.body, exception=exception)
        return HttpResponse(body=response, status_code=HTTPStatus.OK)
