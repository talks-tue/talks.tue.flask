"""added end_timestamp to talk

Revision ID: c78bd7bf1690
Revises: 3f12781ddb4a
Create Date: 2019-06-06 19:25:06.284329

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "c78bd7bf1690"
down_revision = "3f12781ddb4a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("talk", sa.Column("end_timestamp", sa.DateTime(), nullable=True))
    op.alter_column("talk", "timestamp", new_column_name="start_timestamp")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("talk", "end_timestamp")
    op.alter_column("talk", "start_timestamp", new_column_name="timestamp")
    # ### end Alembic commands ###
