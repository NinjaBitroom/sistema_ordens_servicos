"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms import StringField
from wtforms.validators import DataRequired


class MarcaForm(FlaskForm):
    """."""

    nome = StringField("Nome", validators=[DataRequired()])
