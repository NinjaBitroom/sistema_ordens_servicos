"""."""

from sqlalchemy.orm import Mapped, mapped_column

from services.database import DB
from src.models.ordem_de_servico_model import OrdemDeServicoModel
from src.services.base_model import BaseModel


class ContaAReceberModel(DB.Model, BaseModel):
    """."""

    __tablename__ = "Contas a receber"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    ordem_de_servico: Mapped[OrdemDeServicoModel]
    valor: Mapped[float]
