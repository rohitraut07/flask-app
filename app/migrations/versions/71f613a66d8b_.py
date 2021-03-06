"""empty message

Revision ID: 71f613a66d8b
Revises: 8924028b1597
Create Date: 2021-03-11 20:27:27.000320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71f613a66d8b'
down_revision = '8924028b1597'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscribers', sa.Column('public_id', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'subscribers', ['public_id'])
    op.add_column('users', sa.Column('public_id', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'users', ['public_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'public_id')
    op.drop_constraint(None, 'subscribers', type_='unique')
    op.drop_column('subscribers', 'public_id')
    # ### end Alembic commands ###
