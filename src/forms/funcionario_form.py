"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.funcionario_model import FuncionarioModel
from src.services.database import DB

FuncionarioForm: type[FlaskForm] = model_form(
    FuncionarioModel, base_class=FlaskForm, db_session=DB.session
)
