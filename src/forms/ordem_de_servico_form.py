"""."""

from datetime import date

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms import (
    DateField,
    FloatField,
    IntegerField,
    SelectField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired


class OrdemDeServicoForm(FlaskForm):
    """."""

    tecnico_id = IntegerField("Técnico", validators=[DataRequired()])
    cliente_id = SelectField("Cliente", validators=[DataRequired()])
    descricao_do_problema = TextAreaField(
        "Descrição do Problema", validators=[DataRequired()]
    )
    data_ = DateField("Data", validators=[DataRequired()], default=date.today)
    valor_total_da_ordem = FloatField(
        "Valor Total da Ordem", validators=[DataRequired()]
    )
    submit = SubmitField("Salvar")
