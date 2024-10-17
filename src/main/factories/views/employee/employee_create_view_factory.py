"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

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
    mapper = Mapper(
        FuncionarioModel,
        FlaskForm,
        model_form_config={
            "field_args": {
                "cpf": {"label": "CPF"},
                "email": {"label": "E-mail"},
                "telefone_celular": {"label": "Celular"},
                "endereco_rua": {"label": "Rua"},
                "endereco_bairro": {"label": "Bairro"},
                "endereco_numero": {"label": "Número"},
                "endereco_cep": {"label": "CEP"},
                "data_de_cadastro": {"label": "Data de Cadastro no Sistema"},
            },
        },
    )
    controller = EmployeeCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return EmployeeCreateView.as_view(
        "create", controller, mapper, FuncionarioModel
    )
