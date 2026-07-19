"""add last fey columns to posts table

Revision ID: 5d2cfa319a1d
Revises: 151522ae9c3a
Create Date: 2026-07-19 17:50:32.903651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d2cfa319a1d'
down_revision: Union[str, Sequence[str], None] = '151522ae9c3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  nullable=False, server_default=sa.text('NOW()')))


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
