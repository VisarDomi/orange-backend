"""fourth

Revision ID: 2311a668993a
Revises: 9165e18ce33e
Create Date: 2019-06-08 21:02:03.472271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2311a668993a'
down_revision = '9165e18ce33e'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservations', sa.Column('vehicle_type', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservations', 'vehicle_type')
    # ### end Alembic commands ###
