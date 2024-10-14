"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.services.extensions.database import DB
from src.utils.sql_model_converter import SqlModelConverter

CargoDoFuncionarioModelForm = model_form(
    CargoDoFuncionarioModel,
    base_class=FlaskForm,
    db_session=DB.session,
    converter=SqlModelConverter(),
)
