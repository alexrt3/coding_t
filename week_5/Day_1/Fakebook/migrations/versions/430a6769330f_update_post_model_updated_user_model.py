"""update post model. updated user model

Revision ID: 430a6769330f
Revises: 014b174539a9
Create Date: 2021-02-15 02:42:08.475396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '430a6769330f'
down_revision = '014b174539a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('posts', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'post', ['posts'], ['post_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'posts')
    # ### end Alembic commands ###