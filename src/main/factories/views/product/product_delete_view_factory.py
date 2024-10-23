"""."""

from flask.typing import RouteCallable

from src.controllers.product.product_delete_controller import (
    ProductDeleteController,
)
from src.models.produto_model import ProdutoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.product.product_delete_view import ProductDeleteView


def make_product_delete_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(ProdutoModel, DB)
    controller = ProductDeleteController(
        data_access_object, data_access_object
    )
    return ProductDeleteView.as_view("delete", controller)
