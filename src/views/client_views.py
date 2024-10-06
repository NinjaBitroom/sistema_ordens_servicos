"""."""

from flask import flash, redirect, render_template, url_for
from flask.views import MethodView

from src.controllers.client_create_controller import ClientCreateController
from src.forms.client_form import ClientForm


class ClientCreateView(MethodView):
    """."""

    methods = "GET", "POST"

    def __init__(self) -> None:
        """."""
        self.form: ClientForm = ClientForm()
        self.controller = ClientCreateController(self.form)

    def get(self) -> object:
        """."""
        return render_template("client/create.html", form=self.form)

    def post(self) -> object:
        """."""
        response = self.controller.validate()
        if response is None:
            flash("Cliente cadastrado com sucesso")
            return redirect(url_for("root.index"))
        for error in response.args:
            flash(error, "error")
        return render_template("client/create.html", form=self.form)
