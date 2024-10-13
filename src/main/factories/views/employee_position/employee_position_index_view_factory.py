"""."""

from flask.typing import RouteCallable

from src.controllers.employee_position.employee_position_list_controller import (
    EmployeePositionListController,
)
from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.employee_position.employee_position_index_view import (
    EmployeePositionIndexView,
)


def make_employee_position_index_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(CargoDoFuncionarioModel, DB)
    controller = EmployeePositionListController(data_access_object)
    return EmployeePositionIndexView.as_view("index", controller)
