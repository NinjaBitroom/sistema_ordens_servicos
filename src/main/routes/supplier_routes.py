"""."""

from flask import Blueprint

from src.main.factories.views.supplier.supplier_create_view_factory import (
    make_supplier_create_view,
)
from src.main.factories.views.supplier.supplier_delete_view_factory import (
    make_supplier_delete_view,
)
from src.main.factories.views.supplier.supplier_detail_view_factory import (
    make_supplier_detail_view,
)
from src.main.factories.views.supplier.supplier_index_view_factory import (
    make_supplier_index_view,
)

SUPPLIER_BLUEPRINT = Blueprint("supplier", __name__)

SUPPLIER_BLUEPRINT.add_url_rule(
    "/supplier/", view_func=make_supplier_index_view()
)
SUPPLIER_BLUEPRINT.add_url_rule(
    "/supplier/create", view_func=make_supplier_create_view()
)
SUPPLIER_BLUEPRINT.add_url_rule(
    "/supplier/<int:id>", view_func=make_supplier_detail_view()
)
SUPPLIER_BLUEPRINT.add_url_rule(
    "/supplier/delete/<int:id>", view_func=make_supplier_delete_view()
)
