"""Queue locks

Revision ID: 096161ae8c5a
Revises: 3390dcbc6934
Create Date: 2021-12-31 10:07:29.314477

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression


# revision identifiers, used by Alembic.
revision = "096161ae8c5a"
down_revision = "3390dcbc6934"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "queue",
        sa.Column(
            "is_locked",
            sa.Boolean(),
            nullable=False,
            server_default=expression.false(),
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("queue", "is_locked")
    # ### end Alembic commands ###
