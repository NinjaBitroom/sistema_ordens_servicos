"""."""

from flask.typing import RouteCallable

from src.controllers.brand.brand_list_controller import BrandListController
from src.models.marca_model import MarcaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.brand.brand_index_view import BrandIndexView


def make_brand_index_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(MarcaModel, DB)
    controller = BrandListController(data_access_object)
    return BrandIndexView.as_view("index", controller)
