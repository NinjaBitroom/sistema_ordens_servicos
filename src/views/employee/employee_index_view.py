"""."""

from collections.abc import Sequence
from http import HTTPMethod

from flask import render_template
from flask.views import MethodView

from src.models.funcionario_model import FuncionarioModel
from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class EmployeeIndexView(MethodView):
    """."""

    def __init__(
        self,
        controller: Controller[None, Sequence[FuncionarioModel] | Exception],
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=None)
        )
        return render_template("employee/index.html", employees=response.body)
