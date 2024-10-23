"""."""

from flask.typing import RouteCallable

from src.controllers.client.client_detail_controller import (
    ClientDetailController,
)
from src.models.cliente_model import ClienteModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.client.client_detail_view import ClientDetailView


def make_client_detail_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(ClienteModel, DB)
    controller = ClientDetailController(data_access_object)
    return ClientDetailView.as_view("detail", controller)
