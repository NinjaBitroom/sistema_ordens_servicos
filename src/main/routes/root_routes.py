"""."""

from flask import Blueprint

from src.views.index_view import IndexView

ROOT_BLUEPRINT = Blueprint("root", __name__)

ROOT_BLUEPRINT.add_url_rule("/", view_func=IndexView.as_view("index"))
