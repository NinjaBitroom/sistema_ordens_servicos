"""."""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MarcaForm(FlaskForm):
    """."""

    nome = StringField("Nome", validators=[DataRequired()])
