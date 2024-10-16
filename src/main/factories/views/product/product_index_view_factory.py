"""."""

from flask.typing import RouteCallable

from src.controllers.product.product_list_controller import (
    ProductListController,
)
from src.models.produto_model import ProdutoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.product.product_index_view import ProductIndexView


def make_product_index_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(ProdutoModel, DB)
    controller = ProductListController(data_access_object)
    return ProductIndexView.as_view("index", controller)
