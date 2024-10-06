"""."""

from flask import Blueprint

from src.main.factories.views.index_view_factory import make_index_view

ROOT_BLUEPRINT = Blueprint("root", __name__)

ROOT_BLUEPRINT.add_url_rule("/", view_func=make_index_view())
