from services.database import DB
from sqlalchemy.orm import Mapped, mapped_column


class EscolaridadeModel(DB.Model):
    __tablename__ = 'Escolaridades'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    