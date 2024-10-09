"""."""

from flask.typing import RouteCallable

from src.controllers.service_order.service_order_list_controller import (
    ServiceOrderListController,
)
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.service_order.service_order_index_view import (
    ServiceOrderIndexView,
)


def make_service_order_index_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(OrdemDeServicoModel, DB)
    controller = ServiceOrderListController(data_access_object)
    return ServiceOrderIndexView.as_view("index", controller)
