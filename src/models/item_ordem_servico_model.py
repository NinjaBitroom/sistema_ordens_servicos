from models.produto_model import ProdutoModel
from services.database import DB
from sqlalchemy.orm import Mapped, mapped_column


class ItemOrdemServicoModel(DB.Model):
    __tablename__ = 'Itens da ordem de serviço'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    produto: Mapped[ProdutoModel]
    quantidade: Mapped[int]
    valor_total_do_item: Mapped[float]
