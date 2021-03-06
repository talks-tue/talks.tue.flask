"""add location column talk

Revision ID: be10b7e0cf43
Revises: c78bd7bf1690
Create Date: 2019-06-08 06:59:52.831277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "be10b7e0cf43"
down_revision = "c78bd7bf1690"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("talk", sa.Column("location", sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("talk", "location")
    # ### end Alembic commands ###
