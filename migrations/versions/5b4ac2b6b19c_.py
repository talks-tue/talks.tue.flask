"""Rename tag to topic

Revision ID: 5b4ac2b6b19c
Revises: be10b7e0cf43
Create Date: 2019-06-21 13:07:15.536737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5b4ac2b6b19c"
down_revision = "be10b7e0cf43"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table("tag", "topic")
    op.rename_table("talk_tags", "talk_topics")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table("topic", "tag")
    op.rename_table("talk_topics", "talk_tags")
    # ### end Alembic commands ###
