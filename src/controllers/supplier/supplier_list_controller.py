"""."""

from collections.abc import Sequence
from http import HTTPStatus

from src.models.fornecedor_model import FornecedorModel
from src.protocols.controller import Controller
from src.protocols.db.db_get_all_operation import DbGetAllOperation
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse


class SupplierListController(
    Controller[None, Sequence[FornecedorModel] | Exception]
):
    """."""

    def __init__(
        self, db_get_all_operation: DbGetAllOperation[FornecedorModel]
    ) -> None:
        """."""
        self.__DB_GET_ALL_OPERATION = db_get_all_operation

    def handle(
        self, request: HttpRequest[None]
    ) -> HttpResponse[Sequence[FornecedorModel] | Exception]:
        """."""
        _ = request
        response = self.__DB_GET_ALL_OPERATION.get_all()
        return HttpResponse(body=response, status_code=HTTPStatus.OK)
