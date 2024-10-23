"""."""

from flask.typing import RouteCallable

from src.controllers.employee_position.employee_position_delete_controller import (
    EmployeePositionDeleteController,
)
from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.employee_position.employee_position_delete_view import (
    EmployeePositionDeleteView,
)


def make_employee_position_delete_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(CargoDoFuncionarioModel, DB)
    controller = EmployeePositionDeleteController(
        data_access_object, data_access_object
    )
    return EmployeePositionDeleteView.as_view("delete", controller)
