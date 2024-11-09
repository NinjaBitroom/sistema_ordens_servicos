"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # pyright: ignore[reportMissingTypeStubs]

from src.controllers.enterprise.enterprise_create_controller import (
    EnterpriseCreateController,
)
from src.models.empresa_model import EmpresaModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.enterprise.enterprise_create_view import EnterpriseCreateView


def make_enterprise_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(EmpresaModel)
    data_access_object = FlaskSqlAlchemyOperations(EmpresaModel, DB)
    fields = EmpresaModel.model_fields
    mapper = Mapper(
        EmpresaModel,
        FlaskForm,
        {
            "field_args": {
                field: {"label": fields[field].title} for field in fields
            }
        },
    )
    controller = EnterpriseCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return EnterpriseCreateView.as_view(
        "create", controller, mapper, EmpresaModel
    )
