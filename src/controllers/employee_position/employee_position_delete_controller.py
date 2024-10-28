"""."""

from http import HTTPStatus
from typing import Any

from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.protocols.controller import Controller
from src.protocols.db.db_delete_operation import DbDeleteOperation
from src.protocols.db.db_get_one_operation import DbGetOneOperation
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse


class EmployeePositionDeleteController(
    Controller[dict[str, Any], None | Exception]
):
    """."""

    def __init__(
        self,
        db_get_one_operation: DbGetOneOperation[CargoDoFuncionarioModel],
        db_delete_operation: DbDeleteOperation[CargoDoFuncionarioModel],
    ) -> None:
        """."""
        self.__DB_GET_ONE_OPERATION = db_get_one_operation
        self.__DB_DELETE_OPERATION = db_delete_operation

    def handle(
        self, request: HttpRequest[dict[str, Any]]
    ) -> HttpResponse[None | Exception]:
        """."""
        model = self.__DB_GET_ONE_OPERATION.get_one(request.body)
        self.__DB_DELETE_OPERATION.delete(model)
        return HttpResponse(body=None, status_code=HTTPStatus.OK)