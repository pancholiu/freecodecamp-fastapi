"""Add content column to post table

Revision ID: 790859e48469
Revises: 6b8c9e379a50
Create Date: 2026-07-19 00:01:38.767220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '790859e48469'
down_revision: Union[str, Sequence[str], None] = '6b8c9e379a50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
