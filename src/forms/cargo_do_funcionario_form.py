"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.services.database import DB

CargoDoFuncionarioForm = model_form(
    CargoDoFuncionarioModel, base_class=FlaskForm, db_session=DB.session
)
