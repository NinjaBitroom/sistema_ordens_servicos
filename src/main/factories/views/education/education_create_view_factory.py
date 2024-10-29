"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # pyright: ignore[reportMissingTypeStubs]

from src.controllers.education.education_create_controller import (
    EducationCreateController,
)
from src.models.escolaridade_model import EscolaridadeModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.education.education_create_view import EducationCreateView


def make_education_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(EscolaridadeModel)
    data_access_object = FlaskSqlAlchemyOperations(EscolaridadeModel, DB)
    mapper = Mapper(EscolaridadeModel, FlaskForm, {})
    controller = EducationCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return EducationCreateView.as_view(
        "create", controller, mapper, EscolaridadeModel
    )
