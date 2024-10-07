"""."""

from abc import ABC, abstractmethod

from src.protocols.http.http_request import HttpRequest
from src.protocols.http.http_response import HttpResponse


class Controller[TReq, TRes](ABC):
    """."""

    @abstractmethod
    def handle(self, request: HttpRequest[TReq]) -> HttpResponse[TRes]:
        """."""
