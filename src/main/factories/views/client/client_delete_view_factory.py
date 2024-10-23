"""."""

from flask.typing import RouteCallable

from src.controllers.client.client_delete_controller import (
    ClientDeleteController,
)
from src.models.cliente_model import ClienteModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.client.client_delete_view import ClientDeleteView


def make_client_delete_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(ClienteModel, DB)
    controller = ClientDeleteController(data_access_object, data_access_object)
    return ClientDeleteView.as_view("delete", controller)
