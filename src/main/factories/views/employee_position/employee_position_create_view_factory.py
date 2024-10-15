"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.controllers.employee_position.employee_position_create_controller import (
    EmployeePositionCreateController,
)
from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.views.employee_position.employee_position_create_view import (
    EmployeePositionCreateView,
)


def make_employee_position_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation()
    data_access_object = FlaskSqlAlchemyOperations(CargoDoFuncionarioModel, DB)
    mapper = Mapper[FlaskForm, CargoDoFuncionarioModel](
        CargoDoFuncionarioModel
    )
    controller = EmployeePositionCreateController(
        validation, data_access_object, mapper
    )
    return EmployeePositionCreateView.as_view(
        "create",
        controller,
        mapper.model_type_to_form_type(CargoDoFuncionarioModel),
    )
