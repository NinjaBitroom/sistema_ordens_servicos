"""."""

from flask.typing import RouteCallable

from src.controllers.employee_position.employee_position_detail_controller import (
    EmployeePositionDetailController,
)
from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.employee_position.employee_position_detail_view import (
    EmployeePositionDetailView,
)


def make_employee_position_detail_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(CargoDoFuncionarioModel, DB)
    controller = EmployeePositionDetailController(data_access_object)
    return EmployeePositionDetailView.as_view("detail", controller)