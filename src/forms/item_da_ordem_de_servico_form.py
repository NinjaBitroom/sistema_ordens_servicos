"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms import StringField
from wtforms.validators import DataRequired


class ItemDaOrdemDeServicoForm(FlaskForm):
    """."""

    produto = StringField("Produto", validators=[DataRequired()])
    quantidade = StringField("Quantidade", validators=[DataRequired()])
    valor_total_do_item = StringField(
        "Valor Total do Item", validators=[DataRequired()]
    )
