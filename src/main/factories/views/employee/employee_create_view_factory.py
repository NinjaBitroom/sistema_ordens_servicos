"""."""

from flask.typing import RouteCallable

from src.controllers.employee.employee_create_controller import (
    EmployeeCreateController,
)
from src.forms.funcionario_form import FuncionarioForm
from src.models.funcionario_model import FuncionarioModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_operations import FlaskWtfOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.views.employee.employee_create_view import EmployeeCreateView


def make_employee_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation[FuncionarioForm]()
    data_access_object = FlaskSqlAlchemyOperations(FuncionarioModel, DB)
    form_access_object = FlaskWtfOperations(FuncionarioForm)
    controller = EmployeeCreateController(
        validation, data_access_object, form_access_object
    )
    return EmployeeCreateView.as_view("create", controller)