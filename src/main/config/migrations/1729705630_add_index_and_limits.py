"""add index and limits.

Revision ID: 1729705630
Revises: 1729183517
Create Date: 2024-10-23 13:47:10.899005

"""

# ruff: noqa
# pyright: basic

from collections.abc import Sequence

import sqlalchemy as sa
from src.utils import all_types
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1729705630"
down_revision: str | None = "1729183517"
branch_labels: str | Sequence[str] | None = ()
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("ix_Cargos dos funcionários_nome"),
        "Cargos dos funcionários",
        ["nome"],
        unique=False,
    )
    op.create_index(
        op.f("ix_Clientes_nome"), "Clientes", ["nome"], unique=False
    )
    op.create_index(op.f("ix_Empresa_nome"), "Empresa", ["nome"], unique=False)
    op.create_index(
        op.f("ix_Escolaridades_nome"), "Escolaridades", ["nome"], unique=False
    )
    op.create_index(
        op.f("ix_Fornecedores_nome"), "Fornecedores", ["nome"], unique=False
    )
    op.create_index(
        op.f("ix_Funcionários_nome"), "Funcionários", ["nome"], unique=False
    )
    op.create_index(op.f("ix_Marcas_nome"), "Marcas", ["nome"], unique=False)
    op.create_index(
        op.f("ix_Produtos_nome"), "Produtos", ["nome"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_Produtos_nome"), table_name="Produtos")
    op.drop_index(op.f("ix_Marcas_nome"), table_name="Marcas")
    op.drop_index(op.f("ix_Funcionários_nome"), table_name="Funcionários")
    op.drop_index(op.f("ix_Fornecedores_nome"), table_name="Fornecedores")
    op.drop_index(op.f("ix_Escolaridades_nome"), table_name="Escolaridades")
    op.drop_index(op.f("ix_Empresa_nome"), table_name="Empresa")
    op.drop_index(op.f("ix_Clientes_nome"), table_name="Clientes")
    op.drop_index(
        op.f("ix_Cargos dos funcionários_nome"),
        table_name="Cargos dos funcionários",
    )
    # ### end Alembic commands ###
