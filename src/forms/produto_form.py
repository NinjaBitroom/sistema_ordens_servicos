"""."""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ProdutoForm(FlaskForm):
    """."""

    nome = StringField("Nome", validators=[DataRequired()])
    valor_venda = StringField("Valor de Venda", validators=[DataRequired()])
    quantidade_em_estoque = StringField(
        "Quantidade em Estoque", validators=[DataRequired()]
    )
    marca = StringField("Marca", validators=[DataRequired()])
