"""Add hail migration fields

Revision ID: fd02d1c7d64
Revises: 59e5faf237f8
Create Date: 2015-04-15 12:04:43.286358

"""

# revision identifiers, used by Alembic.
revision = 'fd02d1c7d64'
down_revision = '59e5faf237f8'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation_datetime', sa.DateTime(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('client_lon', sa.Float(), nullable=False),
    sa.Column('client_lat', sa.Float(), nullable=False),
    sa.Column('taxi_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('emitted', 'received', 'sent_to_operator', 'received_by_operator', 'received_by_taxi', 'accepted_by_taxi', 'declined_by_taxi', 'incident_client', 'incident_taxi', 'timeout_client', 'timeout_taxi', 'outdated_client', 'outdated_taxi', name='hail_status'), nullable=False),
    sa.Column('last_status_change', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hail')
    ### end Alembic commands ###
