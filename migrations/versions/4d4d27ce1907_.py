"""empty message

Revision ID: 4d4d27ce1907
Revises: 7315a1367475
Create Date: 2019-05-14 17:46:50.568484

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4d4d27ce1907'
down_revision = '7315a1367475'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cards', sa.Column('assigned_to', sa.String(length=255), nullable=True, server_default=sa.text("''")))
    op.add_column('cards', sa.Column('uuid', sa.String(length=255), nullable=True, server_default=sa.text("''")))
    op.create_index(op.f('ix_cards_uuid'), 'cards', ['uuid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cards_uuid'), table_name='cards')
    op.drop_column('cards', 'uuid')
    op.drop_column('cards', 'assigned_to')
    # ### end Alembic commands ###