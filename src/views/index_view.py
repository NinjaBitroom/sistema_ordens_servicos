"""."""

from flask import render_template
from flask.views import MethodView


class IndexView(MethodView):
    """."""

    def get(self) -> object:
        """."""
        return render_template("pages/index.html")
