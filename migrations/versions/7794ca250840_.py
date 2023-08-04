"""empty message

Revision ID: 7794ca250840
Revises: 0c86315bfd0c
Create Date: 2023-08-03 18:03:21.296198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7794ca250840'
down_revision = '0c86315bfd0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=80), nullable=False))
        batch_op.create_unique_constraint("email", ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_constraint("email", type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###