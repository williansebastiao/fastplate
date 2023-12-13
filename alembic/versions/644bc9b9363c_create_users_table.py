"""create users table

Revision ID: 644bc9b9363c
Revises: 
Create Date: 2023-12-13 13:50:18.332721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '644bc9b9363c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(30)),
        sa.Column('last_name', sa.String(100)),
        sa.Column('email', sa.String(120), unique=True),
        sa.Column('cpf', sa.String(11), unique=True),
        sa.Column('avatar', sa.String(255), nullable=True),
        sa.Column('active', sa.Boolean, default=True),
        sa.Column('created_at', sa.DateTime(timezone=True)),
        sa.Column('updated_at', sa.DateTime(timezone=True)),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('users')
