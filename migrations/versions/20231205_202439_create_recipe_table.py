"""create recipe table

Revision ID: 9bfed6c75059
Revises: ffdc0a98111c
Create Date: 2023-12-05 20:24:39.598555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bfed6c75059'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=75), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('prepTime', sa.String(length=10), nullable=True),
    sa.Column('totalTime', sa.String(length=10), nullable=True),
    sa.Column('servings', sa.Integer(), nullable=False),
    sa.Column('directions', sa.Text(), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('source', sa.String(length=150), nullable=True),
    sa.Column('img_url', sa.String(length=255), nullable=True),
    sa.Column('ingredients', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes')
    # ### end Alembic commands ###