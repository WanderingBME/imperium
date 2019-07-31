"""empty message

Revision ID: 2e4dc45970d9
Revises: 7a35c4919e28
Create Date: 2019-07-28 20:31:35.517996

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from models.data_models import TextPickleType

# revision identifiers, used by Alembic.
revision = '2e4dc45970d9'
down_revision = '7a35c4919e28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('decks', 'starter_cards')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('decks', sa.Column('starter_cards', TextPickleType(), nullable=False))
    # ### end Alembic commands ###
