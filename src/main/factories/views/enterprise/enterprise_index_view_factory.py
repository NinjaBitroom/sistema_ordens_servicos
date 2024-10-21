"""."""

from flask.typing import RouteCallable

from src.controllers.enterprise.enterprise_list_controller import (
    EnterpriseListController,
)
from src.models.empresa_model import EmpresaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.enterprise.enterprise_index_view import EnterpriseIndexView


def make_enterprise_index_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(EmpresaModel, DB)
    controller = EnterpriseListController(data_access_object)
    return EnterpriseIndexView.as_view("index", controller)
