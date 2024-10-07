"""."""

from flask.typing import RouteCallable

from src.controllers.client_list_controller import ClientListController
from src.models.cliente_model import ClienteModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.client.client_index_view import ClientIndexView


def make_client_index_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(ClienteModel, DB)
    controller = ClientListController(data_access_object)
    return ClientIndexView.as_view("index", controller)
