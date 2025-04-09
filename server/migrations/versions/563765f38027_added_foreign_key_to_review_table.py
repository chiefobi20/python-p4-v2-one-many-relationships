"""Added foreign key to Review table

Revision ID: 563765f38027
Revises: 5f8362fdcea8
Create Date: 2025-04-09 12:58:32.792140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '563765f38027'
down_revision = '5f8362fdcea8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
