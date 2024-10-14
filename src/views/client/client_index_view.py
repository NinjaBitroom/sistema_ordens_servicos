"""."""

from collections.abc import Sequence
from http import HTTPMethod

from flask import render_template
from flask.views import MethodView

from src.models.cliente_model import ClienteModel
from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class ClientIndexView(MethodView):
    """."""

    def __init__(
        self, controller: Controller[None, Sequence[ClienteModel] | Exception]
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=None)
        )
        return render_template(
            "pages/client/index.html", clients=response.body
        )
