"""."""

from flask.typing import RouteCallable

from src.controllers.brand.brand_detail_controller import BrandDetailController
from src.models.marca_model import MarcaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.brand.brand_detail_view import BrandDetailView


def make_brand_detail_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(MarcaModel, DB)
    controller = BrandDetailController(data_access_object)
    return BrandDetailView.as_view("detail", controller)
