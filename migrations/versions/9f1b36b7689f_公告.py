"""公告

Revision ID: 9f1b36b7689f
Revises: 15ace3ee5f03
Create Date: 2020-02-22 18:17:37.262892

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9f1b36b7689f'
down_revision = '15ace3ee5f03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alert',
                    sa.Column('alert_id', sa.Integer(), nullable=False),
                    sa.Column('alert_time', sa.DateTime(), nullable=True),
                    sa.Column('alert_content', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('alert_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alert')
    # ### end Alembic commands ###
