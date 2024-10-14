"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.funcionario_model import FuncionarioModel
from src.services.extensions.database import DB
from src.utils.sql_model_converter import SqlModelConverter

FuncionarioModelForm: type[FlaskForm] = model_form(
    FuncionarioModel,
    base_class=FlaskForm,
    db_session=DB.session,
    converter=SqlModelConverter(),
    field_args={
        "cpf": {"label": "CPF"},
        "email": {"label": "E-mail"},
        "telefone_celular": {"label": "Celular"},
        "endereco_rua": {"label": "Rua"},
        "endereco_bairro": {"label": "Bairro"},
        "endereco_numero": {"label": "Número"},
        "endereco_cep": {"label": "CEP"},
        "data_de_cadastro": {"label": "Data de Cadastro no Sistema"},
    },
)
