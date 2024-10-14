"""."""

from src.models.funcionario_model import FuncionarioModel
from src.utils.form_from_model import make_form_from_model

FuncionarioModelForm = make_form_from_model(
    FuncionarioModel,
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
