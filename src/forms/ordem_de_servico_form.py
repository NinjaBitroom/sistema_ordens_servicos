"""."""

from flask_wtf import FlaskForm  # type: ignore  # noqa: PGH003
from wtforms_sqlalchemy.orm import model_form  # type: ignore  # noqa: PGH003

from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.extensions.database import DB

OrdemDeServicoForm = model_form(
    OrdemDeServicoModel,
    base_class=FlaskForm,
    db_session=DB.session,
    exclude=["aberto"],
    field_args={
        "tecnico": {"label": "Técnico"},
        "descricao_do_problema": {"label": "Descrição do Problema"},
        "valor_total_da_ordem": {"label": "Valor Total"},
        "data_": {"label": "Data"},
    },
)
