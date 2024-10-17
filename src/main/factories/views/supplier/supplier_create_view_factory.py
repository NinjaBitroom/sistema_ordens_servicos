"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.controllers.supplier.supplier_create_controller import (
    SupplierCreateController,
)
from src.models.fornecedor_model import FornecedorModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.supplier.supplier_create_view import SupplierCreateView


def make_supplier_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(FornecedorModel)
    data_access_object = FlaskSqlAlchemyOperations(FornecedorModel, DB)
    mapper = Mapper(
        FornecedorModel,
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
    controller = SupplierCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return SupplierCreateView.as_view(
        "create", controller, mapper, FornecedorModel
    )
