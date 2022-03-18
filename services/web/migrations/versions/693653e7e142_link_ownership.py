"""Link ownership 

Revision ID: 693653e7e142
Revises: ffc533128925
Create Date: 2022-03-18 02:19:30.263638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '693653e7e142'
down_revision = 'ffc533128925'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shortlinks', sa.Column('created_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'shortlinks', 'users', ['created_by'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shortlinks', type_='foreignkey')
    op.drop_column('shortlinks', 'created_by')
    # ### end Alembic commands ###
