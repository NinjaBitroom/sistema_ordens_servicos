"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.controllers.service_order.service_order_create_controller import (
    ServiceOrderCreateController,
)
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.views.service_order.service_order_create_view import (
    ServiceOrderCreateView,
)


def make_service_order_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation()
    data_access_object = FlaskSqlAlchemyOperations(OrdemDeServicoModel, DB)
    mapper = Mapper[FlaskForm, OrdemDeServicoModel](
        OrdemDeServicoModel,
        exclude=["aberto"],
        field_args={
            "tecnico": {"label": "Técnico"},
            "descricao_do_problema": {"label": "Descrição do Problema"},
            "valor_total_da_ordem": {"label": "Valor Total"},
            "data_": {"label": "Data"},
        },
    )
    controller = ServiceOrderCreateController(
        validation, data_access_object, mapper
    )
    return ServiceOrderCreateView.as_view(
        "create", controller, mapper.model_to_form(OrdemDeServicoModel)
    )
