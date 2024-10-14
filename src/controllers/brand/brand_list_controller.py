"""."""

from collections.abc import Sequence
from http import HTTPStatus

from src.models.marca_model import MarcaModel
from src.protocols.controller import Controller
from src.protocols.db.db_get_all_operation import DbGetAllOperation
from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse


class BrandListController(Controller[None, Sequence[MarcaModel] | Exception]):
    """."""

    def __init__(
        self, db_get_all_operation: DbGetAllOperation[MarcaModel]
    ) -> None:
        """."""
        self.__DB_GET_ALL_OPERATION = db_get_all_operation

    def handle(
        self, request: HttpRequest[None]
    ) -> HttpResponse[Sequence[MarcaModel] | Exception]:
        """."""
        _ = request
        response = self.__DB_GET_ALL_OPERATION.get_all()
        return HttpResponse(body=response, status_code=HTTPStatus.OK)
