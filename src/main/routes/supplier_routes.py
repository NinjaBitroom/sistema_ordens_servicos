"""."""

from flask import Blueprint

from src.main.factories.views.supplier.supplier_index_view_factory import (
    make_supplier_index_view,
)

SUPPLIER_BLUEPRINT = Blueprint("supplier", __name__)

SUPPLIER_BLUEPRINT.add_url_rule(
    "/supplier/", view_func=make_supplier_index_view()
)
