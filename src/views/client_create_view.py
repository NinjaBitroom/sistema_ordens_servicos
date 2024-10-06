"""."""

from typing import cast

from flask import flash, redirect, render_template, url_for
from flask.views import MethodView

from src.controllers.client_create_controller import ClientCreateController
from src.forms.cliente_form import ClienteForm
from src.models.cliente_model import ClienteModel
from src.services.base_model import BaseModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation


class ClientCreateView(MethodView):
    """."""

    methods = "GET", "POST"

    def __init__(self) -> None:
        """."""
        self.form: ClienteForm = ClienteForm()
        flask_sql_alchemy_operations = FlaskSqlAlchemyOperations(
            cast(type[BaseModel], ClienteModel), DB
        )
        flask_wtf_validation = FlaskWtfValidation()
        self.controller = ClientCreateController(
            flask_wtf_validation, flask_sql_alchemy_operations
        )

    def get(self) -> object:
        """."""
        return render_template("client/create.html", form=self.form)

    def post(self) -> object:
        """."""
        response = self.controller.handle(self.form)
        if response is None:
            flash("Cliente cadastrado com sucesso")
            return redirect(url_for("client.index"))
        for error in response.args:
            flash(error, "error")
        return render_template("client/create.html", form=self.form)
