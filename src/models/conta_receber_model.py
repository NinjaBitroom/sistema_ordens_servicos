from models.ordem_servico_model import OrdemServicoModel
from services.database import DB
from sqlalchemy.orm import Mapped, mapped_column


class ContaReceberModel(DB.Model):
    __tablename__ = 'Contas a receber'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    ordem_de_servico: Mapped[OrdemServicoModel]
    valor: Mapped[float]
