"""."""

from flask.typing import RouteCallable

from src.controllers.supplier.supplier_create_controller import (
    SupplierCreateController,
)
from src.models.fornecedor_model import FornecedorModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.views.supplier.supplier_create_view import SupplierCreateView


def make_supplier_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation()
    data_access_object = FlaskSqlAlchemyOperations(FornecedorModel, DB)
    controller = SupplierCreateController(validation, data_access_object)
    mapper = Mapper(
        field_args={
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
    )
    return SupplierCreateView.as_view(
        "create", controller, mapper.model_to_form(FornecedorModel)
    )
