"""."""

from typing import cast

from flask.typing import RouteCallable

from src.controllers.client_create_controller import ClientCreateController
from src.forms.cliente_form import ClienteForm
from src.models.cliente_model import ClienteModel
from src.services.base_model import BaseModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.views.client.client_create_view import ClientCreateView


def make_client_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation()
    model = cast(type[BaseModel], ClienteModel)
    data_access_object = FlaskSqlAlchemyOperations(model, DB)
    controller = ClientCreateController(validation, data_access_object)
    return ClientCreateView.as_view("create", controller, ClienteForm)
