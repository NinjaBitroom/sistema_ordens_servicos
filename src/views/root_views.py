from flask import render_template
from flask.views import View


class IndexView(View):
    methods = ["GET"]

    def dispatch_request(self) -> str:
        return render_template("index.html")
