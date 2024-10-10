"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.fornecedor_model import FornecedorModel
from src.services.database import DB

FornecedorForm = model_form(
    FornecedorModel,
    base_class=FlaskForm,
    db_session=DB.session,
)
