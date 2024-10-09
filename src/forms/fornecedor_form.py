"""."""

from datetime import date

from wtforms import DateField, EmailField, StringField, SubmitField
from wtforms.validators import DataRequired

from src.forms.base.endereco_form import EnderecoForm
from src.forms.base.telefones_form import TelefonesForm


class FornecedorForm(EnderecoForm, TelefonesForm):
    """."""

    nome = StringField("Nome", validators=[DataRequired()])
    cnpj = StringField("CNPJ", validators=[DataRequired()])
    email = EmailField("E-mail", validators=[DataRequired()])
    data_de_cadastro_no_sistema = DateField(
        "Data de Cadastro", validators=[DataRequired()], default=date.today
    )
    submit = SubmitField("Salvar")
