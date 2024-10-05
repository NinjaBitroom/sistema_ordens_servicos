from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import DateField, DateTimeField, SelectField, StringField, EmailField
from wtforms.validators import DataRequired


class ClientForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    gender = SelectField(
        "Gênero",
        choices=[("M", "Masculino"), ("F", "Feminino")],
        validators=[DataRequired()],
    )
    birth_date = DateField("Data de Nascimento", validators=[DataRequired()])
    cpf = StringField("CPF", validators=[DataRequired()])
    registration_date = DateTimeField(
        "Data de Cadastro", validators=[DataRequired()], default=datetime.now
    )
    email = EmailField("E-mail", validators=[DataRequired()])
