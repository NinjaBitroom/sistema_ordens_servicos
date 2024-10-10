"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.cliente_model import ClienteModel
from src.services.database import DB

ClienteForm = model_form(
    ClienteModel, base_class=FlaskForm, db_session=DB.session
)
