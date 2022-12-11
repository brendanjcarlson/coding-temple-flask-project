"""empty message

Revision ID: b41a7e1bf2c3
Revises: 5117edd9ac0c
Create Date: 2022-12-11 10:33:51.141172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b41a7e1bf2c3'
down_revision = '5117edd9ac0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('types', sa.String(length=128), nullable=True),
    sa.Column('abilities', sa.String(length=128), nullable=True),
    sa.Column('sprite', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('pokemon_user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'pokemon_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon_user')
    op.drop_table('user')
    op.drop_table('pokemon')
    # ### end Alembic commands ###
