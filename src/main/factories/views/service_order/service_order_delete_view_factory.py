"""."""

from flask.typing import RouteCallable

from src.controllers.service_order.service_order_delete_controller import (
    ServiceOrderDeleteController,
)
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.service_order.service_order_delete_view import (
    ServiceOrderDeleteView,
)


def make_service_order_delete_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(OrdemDeServicoModel, DB)
    controller = ServiceOrderDeleteController(
        data_access_object, data_access_object
    )
    return ServiceOrderDeleteView.as_view("delete", controller)
