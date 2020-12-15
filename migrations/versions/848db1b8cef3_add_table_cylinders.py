"""add table cylinders

Revision ID: 848db1b8cef3
Revises: fc3e05f4d33c
Create Date: 2020-10-10 22:06:48.786107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '848db1b8cef3'
down_revision = 'fc3e05f4d33c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('СоотношениеОбъёмов',
    sa.Column('ID', sa.Integer(), nullable=False, comment='Первичный ключ'),
    sa.Column('Объём баллона, л', sa.Numeric(4, 2), nullable=False, comment='Объём баллона, л'),
    sa.Column('Давление, ат', sa.Integer, nullable=False, comment='Давление, ат'),
    sa.Column('Объём газа, м3', sa.Numeric(7, 2), nullable=False, comment='Объём газа, м3'),
    sa.Column('Температура, °С', sa.Integer(), nullable=False, comment='Температура, °С'),
    sa.Column('Колличество в связке', sa.Integer(), nullable=False, comment='Колличество в связке'),
    sa.Column('Объём газа в одном баллоне, м3', sa.Numeric(5, 2), nullable=False,
              comment='Объём газа в одном баллоне, м3'),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('СоотношениеОбъёмов')
    # ### end Alembic commands ###
