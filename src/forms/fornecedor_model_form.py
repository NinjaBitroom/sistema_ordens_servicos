"""."""

from src.models.fornecedor_model import FornecedorModel
from src.utils.form_from_model import make_form_from_model

FornecedorModelForm = make_form_from_model(
    FornecedorModel,
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
