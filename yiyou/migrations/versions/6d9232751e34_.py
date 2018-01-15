"""empty message

Revision ID: 6d9232751e34
Revises: 96a7b49e8cce
Create Date: 2018-01-02 14:20:33.334270

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6d9232751e34'
down_revision = '96a7b49e8cce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('foods', 'pictures',
               existing_type=mysql.TEXT(collation='utf8_bin'),
               nullable=True)
    op.alter_column('hotels', 'pictures',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('shops', 'pictures',
               existing_type=mysql.TEXT(collation='utf8_bin'),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('shops', 'pictures',
               existing_type=mysql.TEXT(collation='utf8_bin'),
               nullable=False)
    op.alter_column('hotels', 'pictures',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('foods', 'pictures',
               existing_type=mysql.TEXT(collation='utf8_bin'),
               nullable=False)
    # ### end Alembic commands ###