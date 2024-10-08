"""."""

from http import HTTPStatus

from src.forms.ordem_servico_form import OrdemServicoForm
from src.models.cliente_model import ClienteModel
from src.protocols.controller import Controller
from src.protocols.db.db_add_one_operation import DbAddOneOperation
from src.protocols.db.db_get_all_operation import DbGetAllOperation
from src.protocols.form.choice_injection_data import ChoiceInjectionData
from src.protocols.form.form_create_response import FormCreateResponse
from src.protocols.form.get_form_operation import GetFormOperation
from src.protocols.form.inject_choices_operation import InjectChoicesOperation
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse
from src.protocols.validaton import Validation


class ServiceOrderCreateController(
    Controller[None, FormCreateResponse[OrdemServicoForm]]
):
    """."""

    def __init__(
        self,
        validation: Validation[OrdemServicoForm],
        db_add_one_operation: DbAddOneOperation,
        get_form_operation: GetFormOperation[OrdemServicoForm],
        inject_choices_operation: InjectChoicesOperation[
            tuple[int, str], OrdemServicoForm
        ],
        db_get_all_operation: DbGetAllOperation[ClienteModel],
    ) -> None:
        """."""
        self.__VALIDATION = validation
        self.__DB_ADD_ONE_OPERATION = db_add_one_operation
        self.__GET_FORM_OPERATION = get_form_operation
        self.__INJECT_CHOICES_OPERATION = inject_choices_operation
        self.__DB_GET_ALL_OPERATION = db_get_all_operation

    def handle(
        self, request: HttpRequest[None]
    ) -> HttpResponse[FormCreateResponse[OrdemServicoForm]]:
        """."""
        exception = None
        form = self.__GET_FORM_OPERATION.get_form()
        clients = self.__DB_GET_ALL_OPERATION.get_all()
        self.__INJECT_CHOICES_OPERATION.inject_choices(
            ChoiceInjectionData(
                tuple((c.id, c.nome) for c in clients), "cliente_id", form
            )
        )
        if request.method == "POST":
            exception = self.__VALIDATION.validate(form)
            if exception is None:
                self.__DB_ADD_ONE_OPERATION.add_one(form.data)
        response = FormCreateResponse(form=form, exception=exception)
        return HttpResponse(body=response, status_code=HTTPStatus.OK)
