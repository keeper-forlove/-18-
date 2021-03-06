"""empty message

Revision ID: dd34e75912ef
Revises: 6d9232751e34
Create Date: 2018-01-08 08:30:14.466486

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd34e75912ef'
down_revision = '6d9232751e34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('food_comments', sa.Column('uid', sa.Integer(), nullable=True))
    op.drop_constraint('food_comments_ibfk_2', 'food_comments', type_='foreignkey')
    op.create_foreign_key(None, 'food_comments', 'users', ['uid'], ['id'])
    op.drop_column('food_comments', 'user')
    op.add_column('hotel_comments', sa.Column('uid', sa.Integer(), nullable=True))
    op.drop_constraint('hotel_comments_ibfk_2', 'hotel_comments', type_='foreignkey')
    op.create_foreign_key(None, 'hotel_comments', 'users', ['uid'], ['id'])
    op.drop_column('hotel_comments', 'user')
    op.add_column('shop_comments', sa.Column('uid', sa.Integer(), nullable=True))
    op.drop_constraint('shop_comments_ibfk_2', 'shop_comments', type_='foreignkey')
    op.create_foreign_key(None, 'shop_comments', 'users', ['uid'], ['id'])
    op.drop_column('shop_comments', 'user')
    op.add_column('spot_comments', sa.Column('uid', sa.Integer(), nullable=True))
    op.drop_constraint('spot_comments_ibfk_2', 'spot_comments', type_='foreignkey')
    op.create_foreign_key(None, 'spot_comments', 'users', ['uid'], ['id'])
    op.drop_column('spot_comments', 'user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spot_comments', sa.Column('user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'spot_comments', type_='foreignkey')
    op.create_foreign_key('spot_comments_ibfk_2', 'spot_comments', 'users', ['user'], ['id'])
    op.drop_column('spot_comments', 'uid')
    op.add_column('shop_comments', sa.Column('user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'shop_comments', type_='foreignkey')
    op.create_foreign_key('shop_comments_ibfk_2', 'shop_comments', 'users', ['user'], ['id'])
    op.drop_column('shop_comments', 'uid')
    op.add_column('hotel_comments', sa.Column('user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'hotel_comments', type_='foreignkey')
    op.create_foreign_key('hotel_comments_ibfk_2', 'hotel_comments', 'users', ['user'], ['id'])
    op.drop_column('hotel_comments', 'uid')
    op.add_column('food_comments', sa.Column('user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'food_comments', type_='foreignkey')
    op.create_foreign_key('food_comments_ibfk_2', 'food_comments', 'users', ['user'], ['id'])
    op.drop_column('food_comments', 'uid')
    # ### end Alembic commands ###
