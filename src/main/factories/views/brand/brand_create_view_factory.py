"""."""

from flask.typing import RouteCallable

from src.controllers.brand.brand_create_controller import BrandCreateController
from src.models.marca_model import MarcaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.views.brand.brand_create_view import BrandCreateView


def make_brand_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation()
    data_access_object = FlaskSqlAlchemyOperations(MarcaModel, DB)
    controller = BrandCreateController(validation, data_access_object)
    mapper = Mapper()
    return BrandCreateView.as_view(
        "create", controller, mapper.model_to_form(MarcaModel)
    )
