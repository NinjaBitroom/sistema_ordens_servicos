"""."""

from flask.typing import RouteCallable

from src.controllers.supplier.supplier_create_controller import (
    SupplierCreateController,
)
from src.forms.fornecedor_model_form import FornecedorModelForm
from src.models.fornecedor_model import FornecedorModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.views.supplier.supplier_create_view import SupplierCreateView


def make_supplier_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation()
    data_access_object = FlaskSqlAlchemyOperations(FornecedorModel, DB)
    controller = SupplierCreateController(validation, data_access_object)
    return SupplierCreateView.as_view(
        "create", controller, FornecedorModelForm
    )
