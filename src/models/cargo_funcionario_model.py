from services.database import DB
from sqlalchemy.orm import Mapped, mapped_column


class CargoFuncionarioModel(DB.Model):
    __tablename__ = 'Cargos dos funcionários'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    