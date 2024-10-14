"""."""

from src.models.item_da_ordem_de_servico_model import ItemDaOrdemDeServicoModel
from src.utils.form_from_model import make_form_from_model

ItemDaOrdemDeServicoModelForm = make_form_from_model(ItemDaOrdemDeServicoModel)
