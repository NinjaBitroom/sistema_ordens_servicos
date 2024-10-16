"""."""

from flask import Blueprint

from src.main.factories.views.education.education_create_view_factory import (
    make_education_create_view,
)
from src.main.factories.views.education.education_index_view_factory import (
    make_education_index_view,
)

EDUCATION_BLUEPRINT = Blueprint("education", __name__)

EDUCATION_BLUEPRINT.add_url_rule(
    "/education/create", view_func=make_education_create_view()
)
EDUCATION_BLUEPRINT.add_url_rule(
    "/education/", view_func=make_education_index_view()
)
