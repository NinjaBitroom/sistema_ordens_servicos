"""."""

from flask import flash, redirect, render_template, url_for
from flask.views import MethodView
from wtforms import Form

from src.protocols.controller import Controller


class ClientCreateView(MethodView):
    """."""

    methods = "GET", "POST"

    def __init__(
        self, controller: Controller[Form, Exception | None], form: type[Form]
    ) -> None:
        """."""
        self.__CONTROLLER = controller
        self.__FORM = form()

    def get(self) -> object:
        """."""
        return render_template("client/create.html", form=self.__FORM)

    def post(self) -> object:
        """."""
        response = self.__CONTROLLER.handle(self.__FORM)
        if response is None:
            flash("Cliente cadastrado com sucesso")
            return redirect(url_for("client.index"))
        for error in response.args:
            flash(error, "error")
        return render_template("client/create.html", form=self.__FORM)
