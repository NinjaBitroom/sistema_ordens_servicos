"""."""

from flask.typing import RouteCallable

from src.controllers.enterprise.enterprise_detail_controller import (
    EnterpriseDetailController,
)
from src.models.empresa_model import EmpresaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.enterprise.enterprise_detail_view import EnterpriseDetailView


def make_enterprise_detail_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(EmpresaModel, DB)
    controller = EnterpriseDetailController(data_access_object)
    return EnterpriseDetailView.as_view("detail", controller)
