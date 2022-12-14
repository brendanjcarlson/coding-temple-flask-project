"""empty message

Revision ID: d5ed832ac4af
Revises: bad5bee6310d
Create Date: 2022-12-10 16:00:30.321308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ed832ac4af'
down_revision = 'bad5bee6310d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###
