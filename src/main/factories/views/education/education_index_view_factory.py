"""."""

from flask.typing import RouteCallable

from src.controllers.education.education_list_controller import (
    EducationListController,
)
from src.models.escolaridade_model import EscolaridadeModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.views.education.education_index_view import EducationIndexView


def make_education_index_view() -> RouteCallable:
    """."""
    data_access_object = FlaskSqlAlchemyOperations(EscolaridadeModel, DB)
    controller = EducationListController(data_access_object)
    return EducationIndexView.as_view("index", controller)
