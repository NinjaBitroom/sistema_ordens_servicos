"""."""

from flask.typing import RouteCallable

from src.controllers.supplier.supplier_detail_controller import (
    SupplierDetailController,
)
from src.models.fornecedor_model import FornecedorModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.supplier.supplier_detail_view import SupplierDetailView


def make_supplier_detail_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(FornecedorModel, DB)
    controller = SupplierDetailController(data_access_object)
    return SupplierDetailView.as_view("detail", controller)
