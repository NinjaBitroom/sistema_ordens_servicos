"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms import TelField
from wtforms.validators import DataRequired


class TelefonesForm(FlaskForm):
    """."""

    telefone_fixo = TelField("Telefone Fixo", validators=[DataRequired()])
    telefone_celular = TelField(
        "Telefone Celular", validators=[DataRequired()]
    )
