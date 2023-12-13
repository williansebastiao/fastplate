"""create movies table

Revision ID: 23c3fa903373
Revises: 0ff9db13291a
Create Date: 2023-12-13 13:50:38.398577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23c3fa903373'
down_revision: Union[str, None] = '0ff9db13291a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'movies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(160)),
        sa.Column('year', sa.Integer),
        sa.Column('genre', sa.String(160)),
        sa.Column('plot', sa.Text),
        sa.Column('photo', sa.String(255), nullable=True),
        sa.Column('active', sa.Boolean, default=True),
        sa.Column('created_at', sa.DateTime(timezone=True)),
        sa.Column('updated_at', sa.DateTime(timezone=True)),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('movies')
