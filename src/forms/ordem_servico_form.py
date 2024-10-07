"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms import StringField
from wtforms.validators import DataRequired


class OrdemServicoForm(FlaskForm):
    """."""

    tecnico = StringField("Técnico", validators=[DataRequired()])
    cliente = StringField("Cliente", validators=[DataRequired()])
    descricao_do_problema = StringField(
        "Descrição do Problema", validators=[DataRequired()]
    )
    data_ = StringField("Data", validators=[DataRequired()])
    valor_total_da_ordem = StringField(
        "Valor Total da Ordem", validators=[DataRequired()]
    )
