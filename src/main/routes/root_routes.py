"""."""

from flask import Blueprint

from src.views.index_view import IndexView

root_blueprint = Blueprint("root", __name__)

root_blueprint.add_url_rule("/", view_func=IndexView.as_view("index"))
