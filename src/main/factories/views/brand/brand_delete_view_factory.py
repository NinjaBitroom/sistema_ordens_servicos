"""."""

from flask.typing import RouteCallable

from src.controllers.brand.brand_delete_controller import BrandDeleteController
from src.models.marca_model import MarcaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.brand.brand_delete_view import BrandDeleteView


def make_brand_delete_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(MarcaModel, DB)
    controller = BrandDeleteController(data_access_object, data_access_object)
    return BrandDeleteView.as_view("delete", controller)
