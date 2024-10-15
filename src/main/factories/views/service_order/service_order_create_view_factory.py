"""."""

from flask.typing import RouteCallable

from src.controllers.service_order.service_order_create_controller import (
    ServiceOrderCreateController,
)
from src.forms.ordem_de_servico_model_form import OrdemDeServicoModelForm
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.views.service_order.service_order_create_view import (
    ServiceOrderCreateView,
)


def make_service_order_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation()
    data_access_object = FlaskSqlAlchemyOperations(OrdemDeServicoModel, DB)
    controller = ServiceOrderCreateController(
        validation,
        data_access_object,
    )
    return ServiceOrderCreateView.as_view(
        "create", controller, OrdemDeServicoModelForm
    )
