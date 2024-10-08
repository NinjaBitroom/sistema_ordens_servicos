"""."""

from flask import Blueprint

from src.main.factories.views.service_order.service_order_create_view_factory import (
    make_service_order_create_view,
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
