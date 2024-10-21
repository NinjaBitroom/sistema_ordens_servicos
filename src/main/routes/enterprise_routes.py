"""."""

from flask import Blueprint

from src.main.factories.views.enterprise.enterprise_create_view_factory import (
    make_enterprise_create_view,
)
from src.main.factories.views.enterprise.enterprise_index_view_factory import (
    make_enterprise_index_view,
)

ENTERPRISE_BLUEPRINT = Blueprint("enterprise", __name__)

ENTERPRISE_BLUEPRINT.add_url_rule(
    "/enterprise/", view_func=make_enterprise_index_view()
)
ENTERPRISE_BLUEPRINT.add_url_rule(
    "/enterprise/create", view_func=make_enterprise_create_view()
)
