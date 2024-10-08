"""."""

from datetime import datetime, time
from typing import cast

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms import (
    DateTimeLocalField,
    FloatField,
    IntegerField,
    SelectField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired


class OrdemServicoForm(FlaskForm):
    """."""

    tecnico_id = IntegerField("Técnico", validators=[DataRequired()])
    cliente_id = SelectField("Cliente", validators=[DataRequired()])
    descricao_do_problema = TextAreaField(
        "Descrição do Problema", validators=[DataRequired()]
    )
    data_ = DateTimeLocalField(
        "Data", validators=[DataRequired()], default=cast(time, datetime.now)
    )
    valor_total_da_ordem = FloatField(
        "Valor Total da Ordem", validators=[DataRequired()]
    )
    submit = SubmitField("Salvar")
