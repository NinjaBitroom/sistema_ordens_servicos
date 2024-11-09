"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # pyright: ignore[reportMissingTypeStubs]

from src.controllers.employee.employee_create_controller import (
    EmployeeCreateController,
)
from src.models.funcionario_model import FuncionarioModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.employee.employee_create_view import EmployeeCreateView


def make_employee_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(FuncionarioModel)
    data_access_object = FlaskSqlAlchemyOperations(FuncionarioModel, DB)
    fields = FuncionarioModel.model_fields
    mapper = Mapper(
        FuncionarioModel,
        FlaskForm,
        {
            "field_args": {
                field: {"label": fields[field].title} for field in fields
            }
        },
    )
    controller = EmployeeCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return EmployeeCreateView.as_view(
        "create", controller, mapper, FuncionarioModel
    )
