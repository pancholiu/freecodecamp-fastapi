"""Create post table

Revision ID: 6b8c9e379a50
Revises: 
Create Date: 2026-07-18 23:50:04.043771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b8c9e379a50'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('posts')
