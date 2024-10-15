"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.controllers.brand.brand_create_controller import BrandCreateController
from src.models.marca_model import MarcaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.brand.brand_create_view import BrandCreateView


def make_brand_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(MarcaModel)
    data_access_object = FlaskSqlAlchemyOperations(MarcaModel, DB)
    mapper = Mapper[FlaskForm, MarcaModel](MarcaModel)
    controller = BrandCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return BrandCreateView.as_view(
        "create", controller, mapper.model_type_to_form_type(MarcaModel)
    )
