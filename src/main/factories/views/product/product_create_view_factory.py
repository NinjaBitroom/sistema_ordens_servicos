"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.controllers.product.product_create_controller import (
    ProductCreateController,
)
from src.models.produto_model import ProdutoModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.product.product_create_view import ProductCreateView


def make_product_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(ProdutoModel)
    data_access_object = FlaskSqlAlchemyOperations(ProdutoModel, DB)
    mapper = Mapper(ProdutoModel, FlaskForm, {})
    controller = ProductCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return ProductCreateView.as_view(
        "create", controller, mapper, ProdutoModel
    )
