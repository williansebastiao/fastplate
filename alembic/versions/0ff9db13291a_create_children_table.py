"""create children table

Revision ID: 0ff9db13291a
Revises: 644bc9b9363c
Create Date: 2023-12-13 13:50:31.542595

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ff9db13291a'
down_revision: Union[str, None] = '644bc9b9363c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'children',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('first_name', sa.String(30)),
        sa.Column('last_name', sa.String(100)),
        sa.Column('gender', sa.String(2)),
        sa.Column('birth', sa.Date),
        sa.Column('created_at', sa.DateTime(timezone=True)),
        sa.Column('updated_at', sa.DateTime(timezone=True)),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True)
    )


def downgrade() -> None:
    pass
