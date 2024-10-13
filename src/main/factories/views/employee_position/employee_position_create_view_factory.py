"""."""

from flask.typing import RouteCallable

from src.controllers.employee_position.employee_position_create_controller import (
    EmployeePositionCreateController,
)
from src.forms.cargo_do_funcionario_form import CargoDoFuncionarioForm
from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_operations import FlaskWtfOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.views.employee_position.employee_position_create_view import (
    EmployeePositionCreateView,
)


def make_employee_position_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation[CargoDoFuncionarioForm]()
    data_access_object = FlaskSqlAlchemyOperations(CargoDoFuncionarioModel, DB)
    form_access_object = FlaskWtfOperations(CargoDoFuncionarioForm)
    controller = EmployeePositionCreateController(
        validation, data_access_object, form_access_object
    )
    return EmployeePositionCreateView.as_view("create", controller)
