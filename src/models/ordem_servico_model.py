from datetime import date
from models.cliente_model import ClienteModel
from models.funcionario_model import FuncionarioModel
from services.database import DB
from sqlalchemy.orm import Mapped, mapped_column


class OrdemServicoModel(DB.Model):
    __tablename__ = 'Ordens de serviço'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    tecnico: Mapped[FuncionarioModel]
    cliente: Mapped[ClienteModel]
    descricao_do_problema: Mapped[str]
    data: Mapped[date]
    valor_total_da_ordem: Mapped[float]
