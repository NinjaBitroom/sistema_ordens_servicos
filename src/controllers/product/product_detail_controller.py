"""."""

from http import HTTPStatus
from typing import Any

from src.models.produto_model import ProdutoModel
from src.protocols.controller import Controller
from src.protocols.db.db_get_one_operation import DbGetOneOperation
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse


class ProductDetailController(
    Controller[dict[str, Any], ProdutoModel | Exception]
):
    """."""

    def __init__(
        self, db_get_one_operation: DbGetOneOperation[ProdutoModel]
    ) -> None:
        """."""
        self.__DB_GET_ONE_OPERATION = db_get_one_operation

    def handle(
        self, request: HttpRequest[dict[str, Any]]
    ) -> HttpResponse[ProdutoModel | Exception]:
        """."""
        response = self.__DB_GET_ONE_OPERATION.get_one(request.body)
        return HttpResponse(body=response, status_code=HTTPStatus.OK)
