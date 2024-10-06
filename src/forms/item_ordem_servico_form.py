"""."""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ItemOrdemServicoForm(FlaskForm):
    """."""

    produto = StringField("Produto", validators=[DataRequired()])
    quantidade = StringField("Quantidade", validators=[DataRequired()])
    valor_total_do_item = StringField(
        "Valor Total do Item", validators=[DataRequired()]
    )
