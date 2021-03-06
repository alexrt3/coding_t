"""update post model. updated user model

Revision ID: 0ffb01ebb152
Revises: 430a6769330f
Create Date: 2021-02-15 02:46:31.402430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ffb01ebb152'
down_revision = '430a6769330f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['user_id'])
    op.drop_constraint('user_posts_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('posts', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_posts_fkey', 'user', 'post', ['posts'], ['post_id'])
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###
