"""."""

from src.models.produto_model import ProdutoModel
from src.utils.form_from_model import make_form_from_model

ProdutoModelForm = make_form_from_model(ProdutoModel)
