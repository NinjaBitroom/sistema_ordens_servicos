"""."""

from src.models.escolaridade_model import EscolaridadeModel
from src.utils.form_from_model import make_form_from_model

EscolaridadeModelForm = make_form_from_model(EscolaridadeModel)
