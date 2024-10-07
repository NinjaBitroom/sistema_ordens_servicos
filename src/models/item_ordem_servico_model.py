"""."""

from sqlalchemy.orm import Mapped, mapped_column

from models.produto_model import ProdutoModel
from services.database import DB
from src.services.base_model import BaseModel


class ItemOrdemServicoModel(DB.Model, BaseModel):
    """."""

    __tablename__ = "Itens da ordem de serviço"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    produto: Mapped[ProdutoModel]
    quantidade: Mapped[int]
    valor_total_do_item: Mapped[float]
