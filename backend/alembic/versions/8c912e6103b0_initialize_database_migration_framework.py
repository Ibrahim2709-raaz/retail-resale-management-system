"""initialize database migration framework

Revision ID: 8c912e6103b0
Revises: 
Create Date: 2026-11-02 21:06:10.388439

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = '8c912e6103b0'
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
