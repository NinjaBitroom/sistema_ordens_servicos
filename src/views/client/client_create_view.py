"""."""

from http import HTTPMethod

from flask import flash, redirect, render_template, url_for
from flask.views import MethodView

from src.protocols.controller import Controller
from src.protocols.form.client_create_response import ClientCreateResponse
from src.protocols.http.http_request import HttpRequest


class ClientCreateView(MethodView):
    """."""

    def __init__(
        self, controller: Controller[None, ClientCreateResponse]
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=None)
        )
        return render_template("client/create.html", form=response.body.form)

    def post(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.POST, body=None)
        )
        if response.body.exception is None:
            flash("Cliente cadastrado com sucesso")
            return redirect(url_for("client.index"))
        for error in response.body.exception.args:
            flash(error, "error")
        return render_template("client/create.html", form=response.body.form)
