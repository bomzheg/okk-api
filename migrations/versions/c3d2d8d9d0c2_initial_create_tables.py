"""initial create table

Revision ID: c3d2d8d9d0c2
Revises: 
Create Date: 2020-09-10 12:41:00.565249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3d2d8d9d0c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Партии',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Серия', sa.String(length=10), nullable=False),
    sa.Column('Партия', sa.Date(), nullable=False),
    sa.Column('Суфикс', sa.String(length=5), nullable=True),
    sa.Column('Показать', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Партии')
    # ### end Alembic commands ###