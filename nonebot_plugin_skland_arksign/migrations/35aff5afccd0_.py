"""empty message

Revision ID: 35aff5afccd0
Revises:
Create Date: 2023-09-03 10:15:44.798895

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "35aff5afccd0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "skland_auto_sign_sklandaccount",
        sa.Column("uid", sa.String(), nullable=False),
        sa.Column("qid", sa.Integer(), nullable=False),
        sa.Column("cred", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("uid"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("skland_auto_sign_sklandaccount")
    # ### end Alembic commands ###
