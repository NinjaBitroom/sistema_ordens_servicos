"""."""

from flask import Blueprint

from src.main.factories.views.employee_position.employee_position_create_view_factory import (
    make_employee_position_create_view,
)
from src.main.factories.views.employee_position.employee_position_index_view_factory import (
    make_employee_position_index_view,
)

EMPLOYEE_POSITION_BLUEPRINT = Blueprint("employee_position", __name__)

EMPLOYEE_POSITION_BLUEPRINT.add_url_rule(
    "/employee_position/create", view_func=make_employee_position_create_view()
)
EMPLOYEE_POSITION_BLUEPRINT.add_url_rule(
    "/employee_position/", view_func=make_employee_position_index_view()
)
