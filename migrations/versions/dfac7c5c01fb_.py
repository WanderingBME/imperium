"""empty message

Revision ID: dfac7c5c01fb
Revises: 4359a2680016
Create Date: 2020-01-26 14:58:12.225339

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dfac7c5c01fb'
down_revision = '4359a2680016'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card_templates', 'base_statline')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card_templates', sa.Column('base_statline', mysql.VARCHAR(length=5), nullable=True))
    # ### end Alembic commands ###
