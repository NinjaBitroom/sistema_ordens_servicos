"""."""

from flask import Blueprint

from src.views.client_create_view import ClientCreateView
from src.views.client_index_view import ClientIndexView

CLIENT_BLUEPRINT = Blueprint("client", __name__)

CLIENT_BLUEPRINT.add_url_rule(
    "/client/create", view_func=ClientCreateView.as_view("create")
)
CLIENT_BLUEPRINT.add_url_rule(
    "/client/", view_func=ClientIndexView.as_view("index")
)
