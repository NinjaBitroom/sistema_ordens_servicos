"""."""

from collections.abc import Sequence
from http import HTTPStatus

from src.models.funcionario_model import FuncionarioModel
from src.protocols.controller import Controller
from src.protocols.db.db_get_all_operation import DbGetAllOperation
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse


class EmployeeListController(
    Controller[None, Sequence[FuncionarioModel] | Exception]
):
    """."""

    def __init__(
        self, db_get_all_operation: DbGetAllOperation[FuncionarioModel]
    ) -> None:
        """."""
        self.__DB_GET_ALL_OPERATION = db_get_all_operation

    def handle(
        self, request: HttpRequest[None]
    ) -> HttpResponse[Sequence[FuncionarioModel] | Exception]:
        """."""
        _ = request
        response = self.__DB_GET_ALL_OPERATION.get_all()
        return HttpResponse(body=response, status_code=HTTPStatus.OK)
