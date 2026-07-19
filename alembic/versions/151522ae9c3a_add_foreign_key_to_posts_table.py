"""Add foreign key to posts table

Revision ID: 151522ae9c3a
Revises: 4e9306e33706
Create Date: 2026-07-19 17:38:58.081577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '151522ae9c3a'
down_revision: Union[str, Sequence[str], None] = '4e9306e33706'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'posts_users_id_fk',
        source_table='posts',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )


def downgrade() -> None:
    op.drop_constraint('posts_users_id_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
