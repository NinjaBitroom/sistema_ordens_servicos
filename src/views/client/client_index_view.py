"""."""

from collections.abc import Sequence
from http import HTTPMethod
from typing import Any

from flask import render_template
from flask.views import MethodView

from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class ClientIndexView(MethodView):
    """."""

    def __init__(
        self, controller: Controller[None, Sequence[Any] | Exception]
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=None)
        )
        return render_template("client/index.html", clients=response.body)
