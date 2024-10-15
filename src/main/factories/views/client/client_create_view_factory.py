"""."""

from flask.typing import RouteCallable

from src.controllers.client.client_create_controller import (
    ClientCreateController,
)
from src.models.cliente_model import ClienteModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.views.client.client_create_view import ClientCreateView


def make_client_create_view() -> RouteCallable:
    """."""
    validation = FlaskWtfValidation()
    data_access_object = FlaskSqlAlchemyOperations(ClienteModel, DB)
    controller = ClientCreateController(validation, data_access_object)
    mapper = Mapper(
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
    return ClientCreateView.as_view(
        "create", controller, mapper.model_to_form(ClienteModel)
    )
