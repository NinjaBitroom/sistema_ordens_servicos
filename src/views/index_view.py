"""."""

from flask import render_template
from flask.views import MethodView


class IndexView(MethodView):
    """."""

    methods = ("GET",)

    def get(self) -> object:
        """."""
        return render_template("index.html")
