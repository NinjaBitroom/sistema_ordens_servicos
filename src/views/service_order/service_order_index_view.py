"""."""

from collections.abc import Sequence
from http import HTTPMethod

from flask import render_template
from flask.views import MethodView

from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class ServiceOrderIndexView(MethodView):
    """."""

    def __init__(
        self,
        controller: Controller[
            None, Sequence[OrdemDeServicoModel] | Exception
        ],
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=None)
        )
        return render_template(
            "pages/service_order/index.html", models=response.body
        )
