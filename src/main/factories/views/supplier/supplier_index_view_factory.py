"""."""

from flask.typing import RouteCallable

from src.controllers.supplier.supplier_list_controller import (
    SupplierListController,
)
from src.models.fornecedor_model import FornecedorModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.supplier.supplier_index_view import SupplierIndexView


def make_supplier_index_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(FornecedorModel, DB)
    controller = SupplierListController(data_access_object)
    return SupplierIndexView.as_view("index", controller)
