"""."""

from collections.abc import Sequence
from http import HTTPMethod

from flask import render_template
from flask.views import MethodView

from src.models.marca_model import MarcaModel
from src.protocols.controller import Controller
from src.protocols.http.http_request import HttpRequest


class BrandIndexView(MethodView):
    """."""

    def __init__(
        self, controller: Controller[None, Sequence[MarcaModel] | Exception]
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=None)
        )
        return render_template("pages/brand/index.html", brands=response.body)
