"""."""

from flask import Blueprint

from src.main.factories.views.client.client_create_view_factory import (
    make_client_create_view,
)
from src.main.factories.views.client.client_delete_view_factory import (
    make_client_delete_view,
)
from src.main.factories.views.client.client_detail_view_factory import (
    make_client_detail_view,
)
from src.main.factories.views.client.client_index_view_factory import (
    make_client_index_view,
)

CLIENT_BLUEPRINT = Blueprint("client", __name__)

CLIENT_BLUEPRINT.add_url_rule(
    "/client/create", view_func=make_client_create_view()
)
CLIENT_BLUEPRINT.add_url_rule("/client/", view_func=make_client_index_view())
CLIENT_BLUEPRINT.add_url_rule(
    "/client/<int:id>", view_func=make_client_detail_view()
)
CLIENT_BLUEPRINT.add_url_rule(
    "/client/delete/<int:id>", view_func=make_client_delete_view()
)
