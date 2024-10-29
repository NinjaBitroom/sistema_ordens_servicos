"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # pyright: ignore[reportMissingTypeStubs]

from src.controllers.client.client_create_controller import (
    ClientCreateController,
)
from src.models.cliente_model import ClienteModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.client.client_create_view import ClientCreateView


def make_client_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(ClienteModel)
    data_access_object = FlaskSqlAlchemyOperations(ClienteModel, DB)
    mapper = Mapper(
        ClienteModel,
        FlaskForm,
        model_form_config={
            "field_args": {
                field: {"label": ClienteModel.model_fields[field].title}
                for field in ClienteModel.model_fields
            },
        },
    )
    controller = ClientCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return ClientCreateView.as_view("create", controller, mapper, ClienteModel)
