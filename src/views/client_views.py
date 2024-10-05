from typing import Any

from flask import render_template
from flask.views import MethodView

from src.forms.client_form import ClientForm


class ClientCreateView(MethodView):
    methods = ["GET", "POST"]

    def __init__(self) -> None:
        self.form = ClientForm()

    def get(self) -> Any:
        return render_template("client/create.html", form=self.form)

    def post(self) -> Any:
        pass
