"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.cliente_model import ClienteModel
from src.services.database import DB
from src.utils.sql_model_converter import SqlModelConverter

ClienteForm = model_form(
    ClienteModel,
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
        "data_de_cadastro_no_sistema": {
            "label": "Data de Cadastro no Sistema"
        },
    },
)
