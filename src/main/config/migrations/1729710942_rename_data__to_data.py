"""rename data_ to data.

Revision ID: 1729710942
Revises: 1729705630
Create Date: 2024-10-23 15:15:42.667814

"""

# ruff: noqa
# pyright: basic

from collections.abc import Sequence

import sqlalchemy as sa
from src.utils import all_types
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1729710942"
down_revision: str | None = "1729705630"
branch_labels: str | Sequence[str] | None = ()
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "Ordens de serviço", sa.Column("data", sa.Date(), nullable=False)
    )
    op.drop_column("Ordens de serviço", "data_")
    # ### end Alembic commands ###


def downgrade() -> None:
    """."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "Ordens de serviço", sa.Column("data_", sa.DATE(), nullable=False)
    )
    op.drop_column("Ordens de serviço", "data")
    # ### end Alembic commands ###