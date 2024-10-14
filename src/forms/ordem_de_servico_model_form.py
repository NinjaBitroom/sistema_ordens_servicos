"""."""

from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.utils.form_from_model import make_form_from_model

OrdemDeServicoModelForm = make_form_from_model(
    OrdemDeServicoModel,
    exclude=["aberto"],
    field_args={
        "tecnico": {"label": "Técnico"},
        "descricao_do_problema": {"label": "Descrição do Problema"},
        "valor_total_da_ordem": {"label": "Valor Total"},
        "data_": {"label": "Data"},
    },
)
