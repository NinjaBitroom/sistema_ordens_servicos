"""made changes.

Revision ID: 1728851480
Revises:
Create Date: 2024-10-13 16:31:20.746813

"""

# ruff: noqa
# pyright: basic

from collections.abc import Sequence

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1728851480"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = ("default",)
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Cargos dos funcionários",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sqlmodel.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "Clientes",
        sa.Column("telefone_fixo", sqlmodel.AutoString(), nullable=True),
        sa.Column("telefone_celular", sqlmodel.AutoString(), nullable=True),
        sa.Column("endereco_rua", sqlmodel.AutoString(), nullable=True),
        sa.Column("endereco_bairro", sqlmodel.AutoString(), nullable=True),
        sa.Column("endereco_numero", sa.Integer(), nullable=True),
        sa.Column("endereco_cep", sqlmodel.AutoString(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sqlmodel.AutoString(), nullable=False),
        sa.Column(
            "sexo",
            sa.Enum("Masculino", "Feminino", "Outro", name="genders"),
            nullable=True,
        ),
        sa.Column("nascimento", sa.Date(), nullable=True),
        sa.Column("cpf", sqlmodel.AutoString(), nullable=True),
        sa.Column("data_de_cadastro", sa.Date(), nullable=True),
        sa.Column("email", sqlmodel.AutoString(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "Fornecedores",
        sa.Column("telefone_fixo", sqlmodel.AutoString(), nullable=True),
        sa.Column("telefone_celular", sqlmodel.AutoString(), nullable=True),
        sa.Column("endereco_rua", sqlmodel.AutoString(), nullable=True),
        sa.Column("endereco_bairro", sqlmodel.AutoString(), nullable=True),
        sa.Column("endereco_numero", sa.Integer(), nullable=True),
        sa.Column("endereco_cep", sqlmodel.AutoString(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sqlmodel.AutoString(), nullable=False),
        sa.Column("cnpj", sqlmodel.AutoString(), nullable=False),
        sa.Column("email", sqlmodel.AutoString(), nullable=True),
        sa.Column("data_de_cadastro_no_sistema", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "Funcionários",
        sa.Column("telefone_fixo", sqlmodel.AutoString(), nullable=True),
        sa.Column("telefone_celular", sqlmodel.AutoString(), nullable=True),
        sa.Column("endereco_rua", sqlmodel.AutoString(), nullable=True),
        sa.Column("endereco_bairro", sqlmodel.AutoString(), nullable=True),
        sa.Column("endereco_numero", sa.Integer(), nullable=True),
        sa.Column("endereco_cep", sqlmodel.AutoString(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sqlmodel.AutoString(), nullable=False),
        sa.Column(
            "sexo",
            sa.Enum("Masculino", "Feminino", "Outro", name="genders"),
            nullable=True,
        ),
        sa.Column("nascimento", sa.Date(), nullable=True),
        sa.Column("cpf", sqlmodel.AutoString(), nullable=True),
        sa.Column("email", sqlmodel.AutoString(), nullable=True),
        sa.Column("cargo_id", sa.Integer(), nullable=True),
        sa.Column("data_de_cadastro", sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(
            ["cargo_id"],
            ["Cargos dos funcionários.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "Ordens de serviço",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("tecnico_id", sa.Integer(), nullable=True),
        sa.Column("cliente_id", sa.Integer(), nullable=True),
        sa.Column("descricao_do_problema", sa.Text(), nullable=False),
        sa.Column("valor_total_da_ordem", sa.Float(), nullable=False),
        sa.Column("data_", sa.Date(), nullable=False),
        sa.Column("aberto", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["cliente_id"],
            ["Clientes.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tecnico_id"],
            ["Funcionários.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("Ordens de serviço")
    op.drop_table("Funcionários")
    op.drop_table("Fornecedores")
    op.drop_table("Clientes")
    op.drop_table("Cargos dos funcionários")
    # ### end Alembic commands ###
