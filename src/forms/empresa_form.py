"""."""

from datetime import datetime

from wtforms import DateField, EmailField, StringField
from wtforms.validators import DataRequired

from src.forms.endereco_form import EnderecoForm
from src.forms.telefones_form import TelefonesForm


class EmpresaForm(EnderecoForm, TelefonesForm):
    """."""

    nome = StringField("Nome", validators=[DataRequired()])
    cnpj = StringField("CNPJ", validators=[DataRequired()])
    email = EmailField("E-mail", validators=[DataRequired()])
    data_de_cadastro = DateField(
        "Data de Cadastro", validators=[DataRequired()], default=datetime.now
    )
