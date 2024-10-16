"""."""

from flask import Blueprint

from src.main.factories.views.product.product_create_view_factory import (
    make_product_create_view,
)
from src.main.factories.views.product.product_index_view_factory import (
    make_product_index_view,
)

PRODUCT_BLUEPRINT = Blueprint("product", __name__)

PRODUCT_BLUEPRINT.add_url_rule(
    "/product/create", view_func=make_product_create_view()
)
PRODUCT_BLUEPRINT.add_url_rule(
    "/product/", view_func=make_product_index_view()
)
