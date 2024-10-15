"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003

from src.controllers.client.client_create_controller import (
    ClientCreateController,
)
from src.models.cliente_model import ClienteModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.client.client_create_view import ClientCreateView


def make_client_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(ClienteModel)
    data_access_object = FlaskSqlAlchemyOperations(ClienteModel, DB)
    mapper = Mapper[FlaskForm, ClienteModel](
        ClienteModel,
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
    controller = ClientCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return ClientCreateView.as_view(
        "create", controller, mapper.model_type_to_form_type(ClienteModel)
    )
