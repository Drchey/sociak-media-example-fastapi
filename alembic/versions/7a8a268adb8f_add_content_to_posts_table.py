"""add content to posts table

Revision ID: 7a8a268adb8f
Revises: 97a7c4da2fb8
Create Date: 2022-12-27 09:57:48.246831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a8a268adb8f'
down_revision = '97a7c4da2fb8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
