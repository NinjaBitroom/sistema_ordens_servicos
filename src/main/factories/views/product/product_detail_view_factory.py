"""."""

from flask.typing import RouteCallable

from src.controllers.product.product_detail_controller import (
    ProductDetailController,
)
from src.models.produto_model import ProdutoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.product.product_detail_view import ProductDetailView


def make_product_detail_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(ProdutoModel, DB)
    controller = ProductDetailController(data_access_object)
    return ProductDetailView.as_view("detail", controller)
