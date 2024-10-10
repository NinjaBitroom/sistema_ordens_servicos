"""."""

from datetime import date

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.cliente_model import ClienteModel
from src.models.funcionario_model import FuncionarioModel
from src.services.base_model import BaseModel
from src.services.database import DB


class OrdemDeServicoModel(DB.Model, BaseModel):
    """."""

    __tablename__ = "Ordens de serviço"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    tecnico_id: Mapped[int] = mapped_column(ForeignKey(FuncionarioModel.id))
    tecnico: Mapped[FuncionarioModel] = relationship()
    cliente_id: Mapped[int] = mapped_column(ForeignKey(ClienteModel.id))
    cliente: Mapped[ClienteModel] = relationship()
    descricao_do_problema: Mapped[str] = mapped_column(Text)
    valor_total_da_ordem: Mapped[float]
    data_: Mapped[date] = mapped_column(default_factory=date.today)
    aberto: Mapped[bool] = mapped_column(default=True)
