"""."""

from wtforms import DateField, EmailField, StringField
from wtforms.validators import DataRequired

from src.forms.base.endereco_form import EnderecoForm
from src.forms.base.telefones_form import TelefonesForm


class FuncionarioForm(EnderecoForm, TelefonesForm):
    """."""

    nome = StringField("Nome", validators=[DataRequired()])
    sexo = StringField("Sexo", validators=[DataRequired()])
    nascimento = DateField("Nascimento", validators=[DataRequired()])
    cpf = StringField("CPF", validators=[DataRequired()])
    data_de_cadastro = DateField(
        "Data de Cadastro", validators=[DataRequired()]
    )
    email = EmailField("E-mail", validators=[DataRequired()])
    cargo = StringField("Cargo", validators=[DataRequired()])
