"""."""

from src.models.conta_a_receber_model import ContaAReceberModel
from src.utils.form_from_model import make_form_from_model

ContaAReceberModelForm = make_form_from_model(ContaAReceberModel)
