"""."""

from flask import Blueprint

from src.main.factories.views.enterprise.enterprise_create_view_factory import (
    make_enterprise_create_view,
)
from src.main.factories.views.enterprise.enterprise_delete_view_factory import (
    make_enterprise_delete_view,
)
from src.main.factories.views.enterprise.enterprise_detail_view_factory import (
    make_enterprise_detail_view,
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
ENTERPRISE_BLUEPRINT.add_url_rule(
    "/enterprise/<int:id>", view_func=make_enterprise_detail_view()
)
ENTERPRISE_BLUEPRINT.add_url_rule(
    "/enterprise/delete/<int:id>", view_func=make_enterprise_delete_view()
)
