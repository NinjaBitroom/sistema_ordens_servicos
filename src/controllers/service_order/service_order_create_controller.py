"""."""

from http import HTTPStatus

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.protocols.controller import Controller
from src.protocols.db.db_add_one_operation import DbAddOneOperation
from src.protocols.form.form_create_response import FormCreateResponse
from src.protocols.helpers.form_to_model_operation import FormToModelOperation
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse
from src.protocols.validaton import Validation


class ServiceOrderCreateController(
    Controller[FlaskForm, FormCreateResponse[FlaskForm]]
):
    """."""

    def __init__(
        self,
        flask_form_validation: Validation[FlaskForm],
        db_add_one_operation: DbAddOneOperation[OrdemDeServicoModel],
        form_to_model_operation: FormToModelOperation[
            FlaskForm, OrdemDeServicoModel
        ],
        sql_model_validation: Validation[OrdemDeServicoModel],
    ) -> None:
        """."""
        self.__FLASK_FORM_VALIDATION = flask_form_validation
        self.__DB_ADD_ONE_OPERATION = db_add_one_operation
        self.__FORM_TO_MODEL_OPERATION = form_to_model_operation
        self.__SQL_MODEL_VALIDATION = sql_model_validation

    def handle(
        self, request: HttpRequest[FlaskForm]
    ) -> HttpResponse[FormCreateResponse[FlaskForm]]:
        """."""
        exception = None
        if request.method == "POST":
            exception = self.__FLASK_FORM_VALIDATION.validate(request.body)
            if exception is None:
                model = self.__FORM_TO_MODEL_OPERATION.form_to_model(
                    request.body
                )
                exception = self.__SQL_MODEL_VALIDATION.validate(model)
                if exception is None:
                    self.__DB_ADD_ONE_OPERATION.add_one(model)
        response = FormCreateResponse(form=request.body, exception=exception)
        return HttpResponse(body=response, status_code=HTTPStatus.OK)
