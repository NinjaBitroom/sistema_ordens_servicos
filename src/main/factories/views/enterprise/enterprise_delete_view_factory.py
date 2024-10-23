"""."""

from flask.typing import RouteCallable

from src.controllers.enterprise.enterprise_delete_controller import (
    EnterpriseDeleteController,
)
from src.models.empresa_model import EmpresaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.enterprise.enterprise_delete_view import EnterpriseDeleteView


def make_enterprise_delete_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(EmpresaModel, DB)
    controller = EnterpriseDeleteController(
        data_access_object, data_access_object
    )
    return EnterpriseDeleteView.as_view("delete", controller)
