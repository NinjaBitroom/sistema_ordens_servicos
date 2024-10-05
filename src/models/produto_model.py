from models.marca_model import MarcaModel
from services.database import DB
from sqlalchemy.orm import Mapped, mapped_column


class ProdutoModel(DB.Model):
    __tablename__ = 'Produtos'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    valor_venda: Mapped[float]
    quantidade_em_estoque: Mapped[int]
    marca: Mapped[MarcaModel]
    