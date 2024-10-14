"""."""

from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.utils.form_from_model import (
    make_form_from_model,
)

CargoDoFuncionarioModelForm = make_form_from_model(CargoDoFuncionarioModel)
