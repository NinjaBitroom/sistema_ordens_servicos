"""."""

from flask.typing import RouteCallable

from src.controllers.employee.employee_delete_controller import (
    EmployeeDeleteController,
)
from src.models.funcionario_model import FuncionarioModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.employee.employee_delete_view import EmployeeDeleteView


def make_employee_delete_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(FuncionarioModel, DB)
    controller = EmployeeDeleteController(
        data_access_object, data_access_object
    )
    return EmployeeDeleteView.as_view("delete", controller)
