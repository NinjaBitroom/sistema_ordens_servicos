"""."""

from flask_wtf import FlaskForm
from wtforms import FloatField, StringField
from wtforms.validators import DataRequired


class ContaReceberForm(FlaskForm):
    """."""

    ordem_de_servico = StringField(
        "Ordem de Serviço", validators=[DataRequired()]
    )
    valor = FloatField("Valor", validators=[DataRequired()])
