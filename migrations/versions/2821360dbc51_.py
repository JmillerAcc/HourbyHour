"""empty message

Revision ID: 2821360dbc51
Revises: 008bb0545e03
Create Date: 2023-04-12 12:00:54.562235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2821360dbc51'
down_revision = '008bb0545e03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current_line', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('is_assigned_to_line', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_assigned_to_line')
        batch_op.drop_column('current_line')

    # ### end Alembic commands ###
