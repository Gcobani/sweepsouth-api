"""create_tables
Revision ID: ded5f9299656
Revises:
Create Date: 2021-02-22 22:03:02.337434
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = 'ded5f9299656'
down_revision = None
branch_labels = None
depends_on = None

def create_exchange_rates_table() -> None:
    op.create_table(
        "exchange_rates",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("symbol", sa.Text, nullable=False, index=True),
        sa.Column("rate", sa.Float, nullable=False),
        sa.Column("date", sa.Date, nullable=False)
    )

def upgrade() -> None:
    create_exchange_rates_table()
def downgrade() -> None:
    op.drop_table("exchange_rates")