"""empty message

Revision ID: 0ff11d98cf70
Revises: 3e6e7b86a9ee
Create Date: 2018-01-16 20:41:40.547349

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0ff11d98cf70'
down_revision = '3e6e7b86a9ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('experience', 'uid',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.drop_constraint('experience_ibfk_2', 'experience', type_='foreignkey')
    op.drop_constraint('experience_ibfk_3', 'experience', type_='foreignkey')
    op.drop_column('experience', 'score')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('experience', sa.Column('score', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('experience_ibfk_3', 'experience', 'users', ['uid'], ['id'])
    op.create_foreign_key('experience_ibfk_2', 'experience', 'city', ['city'], ['id'])
    op.alter_column('experience', 'uid',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###