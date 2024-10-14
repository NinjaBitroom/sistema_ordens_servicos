"""."""

from src.models.empresa_model import EmpresaModel
from src.utils.form_from_model import make_form_from_model

EmpresaModelForm = make_form_from_model(EmpresaModel)
