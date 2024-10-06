"""."""

from typing import cast

from flask.typing import RouteCallable

from src.controllers.client_list_controller import ClientListController
from src.models.cliente_model import ClienteModel
from src.services.base_model import BaseModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.client.client_index_view import ClientIndexView


def make_client_index_view() -> RouteCallable:
    """."""
    model = cast(type[BaseModel], ClienteModel)
    data_access_object = FlaskSqlAlchemyOperations(model, DB)
    controller = ClientListController(data_access_object)
    return ClientIndexView.as_view("index", controller)
