"""."""

from flask.typing import RouteCallable

from src.views.client.client_create_view import ClientCreateView


def make_client_create_view() -> RouteCallable:
    """."""
    return ClientCreateView.as_view("create")
