"""."""

from collections.abc import Sequence
from http import HTTPMethod

from flask import render_template
from flask.views import MethodView

from src.models.empresa_model import EmpresaModel
from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class EnterpriseIndexView(MethodView):
    """."""

    def __init__(
        self,
        controller: Controller[None, Sequence[EmpresaModel] | Exception],
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=None)
        )
        return render_template(
            "pages/enterprise/index.html", models=response.body
        )
