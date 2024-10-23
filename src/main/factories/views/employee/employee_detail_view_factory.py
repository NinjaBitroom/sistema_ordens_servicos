"""."""

from flask.typing import RouteCallable

from src.controllers.employee.employee_detail_controller import (
    EmployeeDetailController,
)
from src.models.funcionario_model import FuncionarioModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.employee.employee_detail_view import EmployeeDetailView


def make_employee_detail_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(FuncionarioModel, DB)
    controller = EmployeeDetailController(data_access_object)
    return EmployeeDetailView.as_view("detail", controller)
