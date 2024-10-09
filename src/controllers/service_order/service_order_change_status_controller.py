"""."""

from http import HTTPStatus
from typing import Any

from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.protocols.controller import Controller
from src.protocols.db.db_get_one_operation import DbGetOneOperation
from src.protocols.db.db_update_operation import DbUpdateOperation
from src.protocols.db.update_data import UpdateData
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse


class ServiceOrderChangeStatusController(Controller[dict[str, Any], None]):
    """."""

    def __init__(
        self,
        db_update_operation: DbUpdateOperation[OrdemDeServicoModel],
        db_get_one_operation: DbGetOneOperation[OrdemDeServicoModel],
    ) -> None:
        """."""
        self.__DB_UPDATE_OPERATION = db_update_operation
        self.__DB_GET_ONE_OPERATION = db_get_one_operation

    def handle(
        self, request: HttpRequest[dict[str, Any]]
    ) -> HttpResponse[None]:
        """."""
        model = self.__DB_GET_ONE_OPERATION.get_one(request.body)
        data = {"aberto": not model.aberto}
        self.__DB_UPDATE_OPERATION.update(UpdateData(model, data))
        return HttpResponse(body=None, status_code=HTTPStatus.OK)
