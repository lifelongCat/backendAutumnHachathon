"""database creation

Revision ID: 2a211b9ef4d2
Revises: 
Create Date: 2023-10-22 13:52:08.585024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a211b9ef4d2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('creation_date', sa.String(), nullable=False),
    sa.Column('title', sa.String(length=76), nullable=False),
    sa.Column('subtitle', sa.String(length=76), nullable=True),
    sa.Column('content', sa.String(length=50000), nullable=False),
    sa.Column('theme', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    # ### end Alembic commands ###
