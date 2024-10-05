from services.database import DB
from sqlalchemy.orm import Mapped, mapped_column


class MarcaModel(DB.Model):
    __tablename__ = 'Marcas'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    