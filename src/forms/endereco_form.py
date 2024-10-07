"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class EnderecoForm(FlaskForm):
    """."""

    endereco_rua = StringField("Rua", validators=[DataRequired()])
    endereco_bairro = StringField("Bairro", validators=[DataRequired()])
    endereco_numero = IntegerField("Número", validators=[DataRequired()])
    endereco_cep = StringField("CEP", validators=[DataRequired()])
