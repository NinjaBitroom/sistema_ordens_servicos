"""."""

from http import HTTPMethod

from flask import flash, redirect, render_template, url_for
from flask.views import MethodView
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.models.cliente_model import ClienteModel
from src.protocols.controller import Controller
from src.protocols.form.form_create_response import FormCreateResponse
from src.protocols.helpers.model_type_to_form_type_operation import (
    ModelTypeToFormTypeOperation,
)
from src.protocols.http.http_request import HttpRequest


class ClientCreateView(MethodView):
    """."""

    def __init__(
        self,
        controller: Controller[FlaskForm, FormCreateResponse[FlaskForm]],
        model_type_to_form_type_operation: ModelTypeToFormTypeOperation[
            ClienteModel, FlaskForm
        ],
        model_class: type[ClienteModel],
    ) -> None:
        """."""
        self.__CONTROLLER = controller
        form_class = model_type_to_form_type_operation.model_type_to_form_type(
            model_class
        )
        self.__FORM = form_class()

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=self.__FORM)
        )
        return render_template(
            "pages/client/create.html", form=response.body.form
        )

    def post(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.POST, body=self.__FORM)
        )
        if response.body.exception is None:
            flash("Cliente cadastrado com sucesso")
            return redirect(url_for("client.index"))
        flash(str(response.body.exception), "error")
        return render_template(
            "pages/client/create.html", form=response.body.form
        )
