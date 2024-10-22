"""."""

from flask import Blueprint

from src.main.factories.views.brand.brand_create_view_factory import (
    make_brand_create_view,
)
from src.main.factories.views.brand.brand_detail_view_factory import (
    make_brand_detail_view,
)
from src.main.factories.views.brand.brand_index_view_factory import (
    make_brand_index_view,
)

BRAND_BLUEPRINT = Blueprint("brand", __name__)

BRAND_BLUEPRINT.add_url_rule(
    "/brand/create", view_func=make_brand_create_view()
)
BRAND_BLUEPRINT.add_url_rule("/brand/", view_func=make_brand_index_view())
BRAND_BLUEPRINT.add_url_rule(
    "/brand/<int:id>", view_func=make_brand_detail_view()
)
