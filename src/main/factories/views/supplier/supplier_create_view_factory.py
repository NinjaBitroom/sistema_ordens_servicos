"""."""

from flask.typing import RouteCallable

from src.controllers.supplier.supplier_create_controller import (
    SupplierCreateController,
)
from src.forms.fornecedor_form import FornecedorForm
from src.models.fornecedor_model import FornecedorModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_operations import FlaskWtfOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.views.supplier.supplier_create_view import SupplierCreateView


def make_supplier_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation[FornecedorForm]()
    data_access_object = FlaskSqlAlchemyOperations(FornecedorModel, DB)
    form_access_object = FlaskWtfOperations(FornecedorForm)
    controller = SupplierCreateController(
        validation, data_access_object, form_access_object
    )
    return SupplierCreateView.as_view("create", controller)
