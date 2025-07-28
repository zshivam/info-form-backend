"""add image column

Revision ID: 381e22a10c91
Revises: 
Create Date: 2025-07-17 10:09:39.705902
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '381e22a10c91'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('formdata', sa.Column('image', sa.String(length=255), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('formdata', 'image')
