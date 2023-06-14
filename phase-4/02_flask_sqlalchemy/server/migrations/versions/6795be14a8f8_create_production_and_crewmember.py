"""create Production and CrewMember

Revision ID: 6795be14a8f8
Revises: 
Create Date: 2023-06-13 21:06:34.443211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6795be14a8f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('director', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('budget', sa.Float(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('ongoing', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crew_members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('production_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['production_id'], ['productions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crew_members')
    op.drop_table('productions')
    # ### end Alembic commands ###
