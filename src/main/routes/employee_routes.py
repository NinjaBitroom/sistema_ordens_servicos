"""."""

from flask import Blueprint

from src.main.factories.views.employee.employee_create_view_factory import (
    make_employee_create_view,
)
from src.main.factories.views.employee.employee_delete_view_factory import (
    make_employee_delete_view,
)
from src.main.factories.views.employee.employee_detail_view_factory import (
    make_employee_detail_view,
)
from src.main.factories.views.employee.employee_index_view_factory import (
    make_employee_index_view,
)

EMPLOYEE_BLUEPRINT = Blueprint("employee", __name__)

EMPLOYEE_BLUEPRINT.add_url_rule(
    "/employee/create", view_func=make_employee_create_view()
)
EMPLOYEE_BLUEPRINT.add_url_rule(
    "/employee/", view_func=make_employee_index_view()
)
EMPLOYEE_BLUEPRINT.add_url_rule(
    "/employee/<int:id>", view_func=make_employee_detail_view()
)
EMPLOYEE_BLUEPRINT.add_url_rule(
    "/employee/delete/<int:id>", view_func=make_employee_delete_view()
)
