"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # pyright: ignore[reportMissingTypeStubs]

from src.controllers.enterprise.enterprise_create_controller import (
    EnterpriseCreateController,
)
from src.models.empresa_model import EmpresaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.enterprise.enterprise_create_view import EnterpriseCreateView


def make_enterprise_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(EmpresaModel)
    data_access_object = FlaskSqlAlchemyOperations(EmpresaModel, DB)
    mapper = Mapper(
        EmpresaModel,
        FlaskForm,
        model_form_config={
            "field_args": {
                "cnpj": {"label": "CNPJ"},
                "email": {"label": "E-mail"},
                "telefone_celular": {"label": "Celular"},
                "endereco_rua": {"label": "Rua"},
                "endereco_bairro": {"label": "Bairro"},
                "endereco_numero": {"label": "Número"},
                "endereco_cep": {"label": "CEP"},
                "data_de_cadastro_no_sistema": {
                    "label": "Data de Cadastro no Sistema"
                },
            },
        },
    )
    controller = EnterpriseCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return EnterpriseCreateView.as_view(
        "create", controller, mapper, EmpresaModel
    )
