"""add path for passport and approve

Revision ID: fc3e05f4d33c
Revises: abc645da5772
Create Date: 2020-10-06 15:04:09.555521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc3e05f4d33c'
down_revision = 'abc645da5772'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Партии', sa.Column('approve_path', sa.String(length=256), nullable=True))
    op.add_column('Партии', sa.Column('passport_path', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Партии', 'passport_path')
    op.drop_column('Партии', 'approve_path')
    # ### end Alembic commands ###
