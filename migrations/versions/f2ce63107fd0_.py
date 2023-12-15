"""empty message

Revision ID: f2ce63107fd0
Revises: 
Create Date: 2023-12-15 11:01:52.437796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f2ce63107fd0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "flats",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=128), nullable=False),
        sa.Column("location", sa.String(length=128), nullable=False),
        sa.Column("image_url", sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("flats")
