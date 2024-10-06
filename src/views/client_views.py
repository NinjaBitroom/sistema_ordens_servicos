"""."""

from flask import flash, redirect, render_template, url_for
from flask.views import MethodView

from src.controllers.client_create_controller import ClientCreateController
from src.forms.cliente_form import ClienteForm
from src.models.cliente_model import ClienteModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations


class ClientCreateView(MethodView):
    """."""

    methods = "GET", "POST"

    def __init__(self) -> None:
        """."""
        self.form: ClienteForm = ClienteForm()
        flask_sql_alchemy_operations = FlaskSqlAlchemyOperations(
            ClienteModel, DB
        )
        self.controller = ClientCreateController(
            self.form, flask_sql_alchemy_operations
        )

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
