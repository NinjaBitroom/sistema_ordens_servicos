"""."""

from flask.typing import RouteCallable

from src.controllers.education.education_delete_controller import (
    EducationDeleteController,
)
from src.models.escolaridade_model import EscolaridadeModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.education.education_delete_view import EducationDeleteView


def make_education_delete_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(EscolaridadeModel, DB)
    controller = EducationDeleteController(
        data_access_object, data_access_object
    )
    return EducationDeleteView.as_view("delete", controller)
