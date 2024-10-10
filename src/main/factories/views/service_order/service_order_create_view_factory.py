"""."""

from flask.typing import RouteCallable

from src.controllers.service_order.service_order_create_controller import (
    ServiceOrderCreateController,
)
from src.forms.ordem_de_servico_form import OrdemDeServicoForm
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_operations import FlaskWtfOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.views.service_order.service_order_create_view import (
    ServiceOrderCreateView,
)


def make_service_order_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation[OrdemDeServicoForm]()
    service_order_data_access_object = FlaskSqlAlchemyOperations(
        OrdemDeServicoModel, DB
    )
    form_access_object = FlaskWtfOperations(OrdemDeServicoForm)
    controller = ServiceOrderCreateController(
        validation,
        service_order_data_access_object,
        form_access_object,
    )
    return ServiceOrderCreateView.as_view("create", controller)
