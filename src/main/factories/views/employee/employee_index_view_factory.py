"""."""

from flask.typing import RouteCallable

from src.controllers.employee.employee_list_controller import (
    EmployeeListController,
)
from src.models.funcionario_model import FuncionarioModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.employee.employee_index_view import EmployeeIndexView


def make_employee_index_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(FuncionarioModel, DB)
    controller = EmployeeListController(data_access_object)
    return EmployeeIndexView.as_view("index", controller)
