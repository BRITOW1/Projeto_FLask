"""empty message

Revision ID: e478c0bc9dcd
Revises: a93d5fdfc35c
Create Date: 2021-11-02 17:09:24.783499

"""

# revision identifiers, used by Alembic.
revision = 'e478c0bc9dcd'
down_revision = 'a93d5fdfc35c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('motivos',
    sa.Column('codigo', sa.String(), nullable=False),
    sa.Column('macro', sa.String(), nullable=True),
    sa.Column('micro', sa.String(), nullable=True),
    sa.Column('explicacao', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('codigo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('motivos')
    # ### end Alembic commands ###