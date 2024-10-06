"""."""

from flask.typing import RouteCallable

from src.views.client.client_index_view import ClientIndexView


def make_client_index_view() -> RouteCallable:
    """."""
    return ClientIndexView.as_view("index")
