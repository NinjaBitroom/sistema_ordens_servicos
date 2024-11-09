"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # pyright: ignore[reportMissingTypeStubs]

from src.controllers.service_order.service_order_create_controller import (
    ServiceOrderCreateController,
)
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.service_order.service_order_create_view import (
    ServiceOrderCreateView,
)


def make_service_order_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(OrdemDeServicoModel)
    data_access_object = FlaskSqlAlchemyOperations(OrdemDeServicoModel, DB)
    fields = OrdemDeServicoModel.model_fields
    mapper = Mapper(
        OrdemDeServicoModel,
        FlaskForm,
        {
            "exclude": ["aberto"],
            "field_args": {
                field: {"label": fields[field].title} for field in fields
            },
        },
    )
    controller = ServiceOrderCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return ServiceOrderCreateView.as_view(
        "create", controller, mapper, OrdemDeServicoModel
    )
