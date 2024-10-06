"""."""

from typing import cast

from flask import render_template
from flask.views import MethodView

from src.controllers.client_list_controller import ClientListController
from src.models.cliente_model import ClienteModel
from src.services.base_model import BaseModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations


class ClientIndexView(MethodView):
    """."""

    methods = ("GET",)

    def __init__(self) -> None:
        """."""
        self.controller = ClientListController(
            FlaskSqlAlchemyOperations(cast(type[BaseModel], ClienteModel), DB)
        )

    def get(self) -> object:
        """."""
        response = self.controller.handle()
        return render_template("client/index.html", clients=response)
