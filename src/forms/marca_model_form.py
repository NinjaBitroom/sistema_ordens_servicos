"""."""

from src.models.marca_model import MarcaModel
from src.utils.form_from_model import make_form_from_model

MarcaModelForm = make_form_from_model(MarcaModel)
