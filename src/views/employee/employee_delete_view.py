"""."""

from http import HTTPMethod
from typing import Any

from flask import flash, redirect, url_for
from flask.views import MethodView

from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class EmployeeDeleteView(MethodView):
    """."""

    def __init__(
        self, controller: Controller[dict[str, Any], None | Exception]
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def post(self, **kwargs: object) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.POST, body={"id": kwargs.get("id")})
        )
        if isinstance(response.body, Exception):
            flash(str(response.body), "error")
        return redirect(url_for("employee.index"))
