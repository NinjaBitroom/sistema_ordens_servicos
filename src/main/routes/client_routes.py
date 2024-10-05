from flask import Blueprint

from src.views.client_views import ClientCreateView

client_blueprint = Blueprint("client", __name__)

client_blueprint.add_url_rule(
    "/client/create", view_func=ClientCreateView.as_view("create")
)
