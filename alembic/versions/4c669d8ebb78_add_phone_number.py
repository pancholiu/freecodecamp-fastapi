"""add phone number

Revision ID: 4c669d8ebb78
Revises: 8c859f556417
Create Date: 2026-07-19 18:09:39.948850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c669d8ebb78'
down_revision: Union[str, Sequence[str], None] = '8c859f556417'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column(
        'phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
