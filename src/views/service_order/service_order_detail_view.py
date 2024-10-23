"""."""

from http import HTTPMethod
from typing import Any

from flask import render_template
from flask.views import MethodView

from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class ServiceOrderDetailView(MethodView):
    """."""

    def __init__(
        self,
        controller: Controller[
            dict[str, Any], OrdemDeServicoModel | Exception
        ],
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self, *args: object, **kwargs: object) -> object:
        """."""
        _ = args
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body={"id": kwargs["id"]})
        )
        return render_template(
            "pages/service_order/detail.html", model=response.body
        )
