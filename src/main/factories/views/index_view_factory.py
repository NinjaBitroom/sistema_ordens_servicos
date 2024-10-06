"""."""

from flask.typing import RouteCallable

from src.views.index_view import IndexView


def make_index_view() -> RouteCallable:
    """."""
    return IndexView.as_view("index")
