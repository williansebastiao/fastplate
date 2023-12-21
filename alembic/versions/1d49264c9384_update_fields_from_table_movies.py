"""update fields from table movies

Revision ID: 1d49264c9384
Revises: 23c3fa903373
Create Date: 2023-12-20 23:49:56.017124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d49264c9384'
down_revision: Union[str, None] = '23c3fa903373'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('movies', 'created_at', type_=sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False)
    op.alter_column('movies', 'updated_at', type_=sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False)
    op.alter_column('movies', 'deleted_at', type_=sa.DateTime(), nullable=True)

def downgrade() -> None:
    pass
