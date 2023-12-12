"""create addresses table

Revision ID: 609b500a2a78
Revises: 4fe7633497a3
Create Date: 2023-12-12 19:26:19.058773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '609b500a2a78'
down_revision: Union[str, None] = '4fe7633497a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'addresses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('zipcode', sa.String(10)),
        sa.Column('city', sa.String(50)),
        sa.Column('state', sa.String(50)),
        sa.Column('number', sa.Integer),
        sa.Column('complement', sa.String(100), nullable=True),
        sa.Column('address', sa.String(100))
    )


def downgrade() -> None:
    op.drop_table('addresses')
