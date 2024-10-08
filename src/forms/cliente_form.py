"""."""

from datetime import datetime

from wtforms import (
    DateField,
    EmailField,
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired

from src.forms.endereco_form import EnderecoForm
from src.forms.telefones_form import TelefonesForm


class ClienteForm(EnderecoForm, TelefonesForm):
    """."""

    nome = StringField("Nome", validators=[DataRequired()])
    sexo = SelectField(
        "Gênero",
        choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")],
        validators=[DataRequired()],
    )
    nascimento = DateField("Data de Nascimento", validators=[DataRequired()])
    cpf = StringField("CPF", validators=[DataRequired()])
    data_de_cadastro = DateField(
        "Data de Cadastro", validators=[DataRequired()], default=datetime.now
    )
    email = EmailField("E-mail", validators=[DataRequired()])
    submit = SubmitField("Salvar")
