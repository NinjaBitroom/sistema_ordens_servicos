"""."""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TelefonesForm(FlaskForm):
    """."""

    telefone_fixo = StringField("Telefone Fixo", validators=[DataRequired()])
    telefone_celular = StringField(
        "Telefone Celular", validators=[DataRequired()]
    )
