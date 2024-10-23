"""."""

from flask.typing import RouteCallable

from src.controllers.service_order.service_order_detail_controller import (
    ServiceOrderDetailController,
)
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.service_order.service_order_detail_view import (
    ServiceOrderDetailView,
)


def make_service_order_detail_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(OrdemDeServicoModel, DB)
    controller = ServiceOrderDetailController(data_access_object)
    return ServiceOrderDetailView.as_view("detail", controller)
