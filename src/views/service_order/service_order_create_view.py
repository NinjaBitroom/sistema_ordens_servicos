"""."""

from http import HTTPMethod

from flask import flash, redirect, render_template, url_for
from flask.views import MethodView
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.protocols.controller import Controller
from src.protocols.form.form_create_response import FormCreateResponse
from src.protocols.http.http_request import HttpRequest


class ServiceOrderCreateView(MethodView):
    """."""

    def __init__(
        self,
        controller: Controller[None, FormCreateResponse[FlaskForm]],
    ) -> None:
        """."""
        self.__CONTROLLER = controller

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=None)
        )
        return render_template(
            "service_order/create.html", form=response.body.form
        )

    def post(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.POST, body=None)
        )
        if response.body.exception is None:
            flash("Ordem de Serviço cadastrada com sucesso")
            return redirect(url_for("service_order.index"))
        for error in response.body.exception.args:
            flash(error, "error")
        return render_template(
            "service_order/create.html", form=response.body.form
        )
