"""."""

from http import HTTPMethod

from flask import flash, redirect, render_template, url_for
from flask.views import MethodView
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.protocols.controller import Controller
from src.protocols.form.form_create_response import FormCreateResponse
from src.protocols.http.http_request import HttpRequest


class EducationCreateView(MethodView):
    """."""

    def __init__(
        self,
        controller: Controller[FlaskForm, FormCreateResponse[FlaskForm]],
        form: type[FlaskForm],
    ) -> None:
        """."""
        self.__CONTROLLER = controller
        self.__FORM = form()

    def get(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.GET, body=self.__FORM)
        )
        return render_template(
            "pages/education/create.html", form=response.body.form
        )

    def post(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(
            HttpRequest(method=HTTPMethod.POST, body=self.__FORM)
        )
        if response.body.exception is None:
            flash("Escolaridade cadastrada com sucesso")
            return redirect(url_for("education.index"))
        flash(str(response.body.exception), "error")
        return render_template(
            "pages/education/create.html", form=response.body.form
        )
