"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.fornecedor_model import FornecedorModel
from src.services.database import DB

FornecedorForm = model_form(
    FornecedorModel,
    base_class=FlaskForm,
    db_session=DB.session,
    field_args={
        "cnpj": {"label": "CNPJ"},
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
