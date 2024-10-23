"""."""

from http import HTTPMethod
from typing import Any

from flask import render_template
from flask.views import MethodView

from src.models.produto_model import ProdutoModel
from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class ProductDetailView(MethodView):
    """."""

    def __init__(
        self, controller: Controller[dict[str, Any], ProdutoModel | Exception]
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
            "pages/product/detail.html", model=response.body
        )
