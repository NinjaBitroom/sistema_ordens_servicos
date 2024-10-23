"""."""

from flask.typing import RouteCallable

from src.controllers.education.education_detail_controller import (
    EducationDetailController,
)
from src.models.escolaridade_model import EscolaridadeModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.education.education_detail_view import EducationDetailView


def make_education_detail_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(EscolaridadeModel, DB)
    controller = EducationDetailController(data_access_object)
    return EducationDetailView.as_view("detail", controller)
