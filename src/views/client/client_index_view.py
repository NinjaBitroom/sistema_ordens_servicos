"""."""

from collections.abc import Sequence
from typing import Any

from flask import render_template
from flask.views import MethodView

from src.protocols.controller import Controller


class ClientIndexView(MethodView):
    """."""

    methods = ("GET",)

    def __init__(
        self, controller: Controller[None, Sequence[Any] | Exception]
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(None)
        return render_template("client/index.html", clients=response)
