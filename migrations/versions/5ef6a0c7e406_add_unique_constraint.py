"""add unique constraint

Revision ID: 5ef6a0c7e406
Revises: 848db1b8cef3
Create Date: 2020-11-07 06:21:29.911741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ef6a0c7e406'
down_revision = '848db1b8cef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Партии', schema=None) as batch_op:
        batch_op.create_unique_constraint('_partia_suffix_uc', ['Партия', 'Суфикс'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Партии', schema=None) as batch_op:
        batch_op.drop_constraint('_partia_suffix_uc', type_='unique')

    # ### end Alembic commands ###
