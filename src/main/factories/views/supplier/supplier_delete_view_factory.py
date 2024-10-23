"""."""

from flask.typing import RouteCallable

from src.controllers.supplier.supplier_delete_controller import (
    SupplierDeleteController,
)
from src.models.fornecedor_model import FornecedorModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.supplier.supplier_delete_view import SupplierDeleteView


def make_supplier_delete_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(FornecedorModel, DB)
    controller = SupplierDeleteController(
        data_access_object, data_access_object
    )
    return SupplierDeleteView.as_view("delete", controller)
