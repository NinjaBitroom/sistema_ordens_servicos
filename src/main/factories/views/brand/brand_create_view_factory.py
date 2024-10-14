"""."""

from flask.typing import RouteCallable

from src.controllers.brand.brand_create_controller import BrandCreateController
from src.forms.marca_model_form import MarcaModelForm
from src.models.marca_model import MarcaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_operations import FlaskWtfOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.views.brand.brand_create_view import BrandCreateView


def make_brand_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation[MarcaModelForm]()
    data_access_object = FlaskSqlAlchemyOperations(MarcaModel, DB)
    form_access_object = FlaskWtfOperations(MarcaModelForm)
    controller = BrandCreateController(
        validation, data_access_object, form_access_object
    )
    return BrandCreateView.as_view("create", controller)
