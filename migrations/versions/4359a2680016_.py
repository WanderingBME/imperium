"""empty message

Revision ID: 4359a2680016
Revises: 9f2a481b68bd
Create Date: 2020-01-25 13:50:27.528742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4359a2680016'
down_revision = '9f2a481b68bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card_templates', sa.Column('base_statline', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card_templates', 'base_statline')
    # ### end Alembic commands ###
