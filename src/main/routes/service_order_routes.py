"""."""

from flask import Blueprint

from src.main.factories.views.service_order.service_order_change_status_factory import (
    make_service_order_change_status_view,
)
from src.main.factories.views.service_order.service_order_create_view_factory import (
    make_service_order_create_view,
)
from src.main.factories.views.service_order.service_order_delete_view_factory import (
    make_service_order_delete_view,
)
from src.main.factories.views.service_order.service_order_detail_view_factory import (
    make_service_order_detail_view,
)
from src.main.factories.views.service_order.service_order_index_view_factory import (
    make_service_order_index_view,
)

SERVICE_ORDER_BLUEPRINT = Blueprint("service_order", __name__)

SERVICE_ORDER_BLUEPRINT.add_url_rule(
    "/service_order/", view_func=make_service_order_index_view()
)
SERVICE_ORDER_BLUEPRINT.add_url_rule(
    "/service_order/create", view_func=make_service_order_create_view()
)
SERVICE_ORDER_BLUEPRINT.add_url_rule(
    "/service_order/change_status",
    view_func=make_service_order_change_status_view(),
)
SERVICE_ORDER_BLUEPRINT.add_url_rule(
    "/service_order/<int:id>", view_func=make_service_order_detail_view()
)
SERVICE_ORDER_BLUEPRINT.add_url_rule(
    "/service_order/delete/<int:id>",
    view_func=make_service_order_delete_view(),
)
