from flask import Blueprint

from src.views.root_views import IndexView

root_blueprint = Blueprint("root", __name__)

root_blueprint.add_url_rule("/", view_func=IndexView.as_view("index"))
