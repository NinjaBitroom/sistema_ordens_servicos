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
from src.utils.sql_model_validation import SqlModelValidation
from src.views.employee_position.employee_position_create_view import (
    EmployeePositionCreateView,
)


def make_employee_position_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(CargoDoFuncionarioModel)
    data_access_object = FlaskSqlAlchemyOperations(CargoDoFuncionarioModel, DB)
    mapper = Mapper(CargoDoFuncionarioModel, FlaskForm, {})
    controller = EmployeePositionCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return EmployeePositionCreateView.as_view(
        "create", controller, mapper, CargoDoFuncionarioModel
    )
