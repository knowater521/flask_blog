"""缩略图字段

Revision ID: 15ace3ee5f03
Revises: 
Create Date: 2020-02-16 10:42:38.000257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15ace3ee5f03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('thumb', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_column('thumb')

    # ### end Alembic commands ###
