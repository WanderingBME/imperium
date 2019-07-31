"""empty message

Revision ID: 7a35c4919e28
Revises: 9bed2071be9f
Create Date: 2019-07-28 19:49:09.722820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a35c4919e28'
down_revision = '9bed2071be9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cards', sa.Column('is_starter', sa.Boolean(), nullable=True, server_default=sa.text("0")))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cards', 'is_starter')
    # ### end Alembic commands ###
