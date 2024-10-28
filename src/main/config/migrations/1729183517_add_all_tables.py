"""add all tables.

Revision ID: 1729183517
Revises: 1729092329
Create Date: 2024-10-17 12:45:17.586794

"""

# ruff: noqa
# pyright: basic

from collections.abc import Sequence

import sqlalchemy as sa
from src.utils import all_types
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1729183517"
down_revision: str | None = "1729092329"
branch_labels: str | Sequence[str] | None = ()
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Empresa",
        sa.Column(
            "telefone_fixo",
            all_types.PhoneNumberType(length=20),
            nullable=True,
        ),
        sa.Column(
            "telefone_celular",
            all_types.PhoneNumberType(length=20),
            nullable=True,
        ),
        sa.Column("endereco_rua", all_types.AutoString(), nullable=True),
        sa.Column("endereco_bairro", all_types.AutoString(), nullable=True),
        sa.Column("endereco_numero", sa.Integer(), nullable=True),
        sa.Column("endereco_cep", all_types.AutoString(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", all_types.AutoString(), nullable=False),
        sa.Column("cnpj", all_types.AutoString(), nullable=False),
        sa.Column("email", all_types.EmailType(length=255), nullable=True),
        sa.Column("data_de_cadastro_no_sistema", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "Itens da ordem de serviço",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("produto_id", sa.Integer(), nullable=True),
        sa.Column("quantidade", sa.Integer(), nullable=False),
        sa.Column("valor_total_do_item", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["produto_id"],
            ["Produtos.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "Contas a receber",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ordem_de_servico_id", sa.Integer(), nullable=True),
        sa.Column("valor", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["ordem_de_servico_id"],
            ["Ordens de serviço.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("Contas a receber")
    op.drop_table("Itens da ordem de serviço")
    op.drop_table("Empresa")
    # ### end Alembic commands ###