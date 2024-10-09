"""."""

from http import HTTPMethod
from typing import Any

from flask import redirect, request, url_for
from flask.views import MethodView

from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class ServiceOrderChangeStatusView(MethodView):
    """."""

    def __init__(self, controller: Controller[Any, Any]) -> None:
        """."""
        self.__CONTROLLER = controller

    def post(self) -> object:
        """."""
        self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.POST, body=request.form.to_dict())
        )
        return redirect(url_for("service_order.index"))
