"""."""

from sqlalchemy.orm import Mapped, mapped_column

from models.ordem_servico_model import OrdemServicoModel
from services.database import DB
from src.services.base_model import BaseModel


class ContaReceberModel(DB.Model, BaseModel):
    """."""

    __tablename__ = "Contas a receber"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    ordem_de_servico: Mapped[OrdemServicoModel]
    valor: Mapped[float]
