"""."""

from flask.typing import RouteCallable

from src.controllers.client_create_controller import ClientCreateController
from src.forms.cliente_form import ClienteForm
from src.models.cliente_model import ClienteModel
from src.services.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_operations import FlaskWtfOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.views.client.client_create_view import ClientCreateView


def make_client_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation[ClienteForm]()
    data_access_object = FlaskSqlAlchemyOperations(ClienteModel, DB)
    form_access_object = FlaskWtfOperations[ClienteForm]()
    controller = ClientCreateController(
        validation, data_access_object, form_access_object
    )
    return ClientCreateView.as_view("create", controller)
