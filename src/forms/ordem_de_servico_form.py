"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.database import DB

OrdemDeServicoForm = model_form(
    OrdemDeServicoModel,
    base_class=FlaskForm,
    db_session=DB.session,
    exclude=["aberto"],
)
