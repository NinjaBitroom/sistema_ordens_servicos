"""."""

from flask.typing import RouteCallable
from flask_wtf import FlaskForm  # pyright: ignore[reportMissingTypeStubs]

from src.controllers.supplier.supplier_create_controller import (
    SupplierCreateController,
)
from src.models.fornecedor_model import FornecedorModel
from src.services.extensions.database import DB
from src.services.flask_sql_alchemy_operations import FlaskSqlAlchemyOperations
from src.utils.flask_wtf_validation import FlaskWtfValidation
from src.utils.mapper import Mapper
from src.utils.sql_model_validation import SqlModelValidation
from src.views.supplier.supplier_create_view import SupplierCreateView


def make_supplier_create_view() -> RouteCallable:
    """."""
    flask_wtf_validation = FlaskWtfValidation()
    sql_model_validation = SqlModelValidation(FornecedorModel)
    data_access_object = FlaskSqlAlchemyOperations(FornecedorModel, DB)
    fields = FornecedorModel.model_fields
    mapper = Mapper(
        FornecedorModel,
        FlaskForm,
        {
            "field_args": {
                field: {"label": fields[field].title} for field in fields
            },
        },
    )
    controller = SupplierCreateController(
        flask_wtf_validation, data_access_object, mapper, sql_model_validation
    )
    return SupplierCreateView.as_view(
        "create", controller, mapper, FornecedorModel
    )
