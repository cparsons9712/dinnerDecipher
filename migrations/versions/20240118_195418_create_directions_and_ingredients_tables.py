"""create directions and ingredients tables

Revision ID: ab367670dc43
Revises: 9bfed6c75059
Create Date: 2024-01-18 19:54:18.326801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab367670dc43'
down_revision = '9bfed6c75059'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('directions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipeIngredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('unit', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('recipes', 'directions')
    op.drop_column('recipes', 'ingredients')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('ingredients', sa.TEXT(), nullable=False))
    op.add_column('recipes', sa.Column('directions', sa.TEXT(), nullable=False))
    op.drop_table('recipeIngredients')
    op.drop_table('directions')
    # ### end Alembic commands ###