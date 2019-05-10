"""empty message

Revision ID: ae1ad118d305
Revises: 2edd410e2512
Create Date: 2019-05-09 21:13:44.035015

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ae1ad118d305'
down_revision = '2edd410e2512'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('decks_ibfk_1', 'decks', type_='foreignkey')
    op.drop_column('decks', 'tournament_signup_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('decks', sa.Column('tournament_signup_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key('decks_ibfk_1', 'decks', 'tournaments_signups', ['tournament_signup_id'], ['id'])
    # ### end Alembic commands ###