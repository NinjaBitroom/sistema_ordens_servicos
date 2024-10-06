"""."""

from collections.abc import Sequence
from typing import Any

from src.protocols.controller import Controller
from src.protocols.db.db_get_all_operation import DbGetAllOperation


class ClientListController(Controller):
    """."""

    def __init__(self, db_get_all_operation: DbGetAllOperation) -> None:
        """."""
        self.__DB_GET_ALL_OPERATION = db_get_all_operation

    def handle(self, request: None = None) -> Sequence[Any] | Exception:
        """."""
        _ = request
        return self.__DB_GET_ALL_OPERATION.get_all()
