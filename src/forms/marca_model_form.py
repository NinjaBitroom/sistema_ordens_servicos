"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.marca_model import MarcaModel
from src.services.extensions.database import DB
from src.utils.sql_model_converter import (
    SqlModelConverter,  # type: ignore  # noqa: PGH003
)

MarcaModelForm: type[FlaskForm] = model_form(
    MarcaModel,
    base_class=FlaskForm,
    db_session=DB.session,
    converter=SqlModelConverter(),
)
