from typing import Any

from flask import render_template, flash
from flask.views import MethodView

from src.forms.client_form import ClientForm


class ClientCreateView(MethodView):
    methods = ["GET", "POST"]

    def __init__(self) -> None:
        self.form: ClientForm = ClientForm()

    def get(self) -> Any:
        return render_template("client/create.html", form=self.form)

    def post(self) -> Any:
        if self.form.validate_on_submit():
            return "Success"
        for field, errors in self.form.errors.items():
            for error in errors:
                flash(f"{field}: {error}")
        return render_template("client/create.html", form=self.form)
