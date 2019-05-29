"""third

Revision ID: 82613c03803c
Revises: 1198ee6c2c84
Create Date: 2019-05-30 01:17:12.855291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82613c03803c'
down_revision = '1198ee6c2c84'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('invoices', sa.Column('grand_total', sa.String(), nullable=True))
    op.add_column('invoices', sa.Column('sub_total', sa.String(), nullable=True))
    op.add_column('invoices', sa.Column('tax', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('invoices', 'tax')
    op.drop_column('invoices', 'sub_total')
    op.drop_column('invoices', 'grand_total')
    # ### end Alembic commands ###
