"""."""

from flask_sqlalchemy_lite import SQLAlchemy
from sqlmodel import Session

from src.models.cargo_do_funcionario_model import CargoDoFuncionarioModel
from src.models.cliente_model import ClienteModel
from src.models.conta_a_receber_model import ContaAReceberModel
from src.models.empresa_model import EmpresaModel
from src.models.escolaridade_model import EscolaridadeModel
from src.models.fornecedor_model import FornecedorModel
from src.models.funcionario_model import FuncionarioModel
from src.models.item_da_ordem_de_servico_model import ItemDaOrdemDeServicoModel
from src.models.marca_model import MarcaModel
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.models.produto_model import ProdutoModel

__all__ = (
    "CargoDoFuncionarioModel",
    "ClienteModel",
    "FuncionarioModel",
    "ProdutoModel",
    "ContaAReceberModel",
    "EmpresaModel",
    "EscolaridadeModel",
    "FornecedorModel",
    "ItemDaOrdemDeServicoModel",
    "MarcaModel",
    "OrdemDeServicoModel",
)

DB = SQLAlchemy(session_options={"class_": Session})
