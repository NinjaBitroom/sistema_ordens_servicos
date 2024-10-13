"""."""

from flask.typing import RouteCallable

from src.controllers.service_order.service_order_change_status_controller import (
    ServiceOrderChangeStatusController,
)
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.service_order.service_order_change_status_view import (
    ServiceOrderChangeStatusView,
)


def make_service_order_change_status_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(OrdemDeServicoModel, DB)
    controller = ServiceOrderChangeStatusController(
        data_access_object, data_access_object
    )
    return ServiceOrderChangeStatusView.as_view("change_status", controller)
