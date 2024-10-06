"""."""

from flask import render_template
from flask.views import MethodView


class ClientIndexView(MethodView):
    """."""

    methods = ("GET",)

    def get(self) -> object:
        """."""
        return render_template("client/index.html")
