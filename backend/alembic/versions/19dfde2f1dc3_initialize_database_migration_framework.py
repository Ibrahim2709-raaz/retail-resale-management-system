"""initialize database migration framework

Revision ID: 19dfde2f1dc3
Revises: 8c912e6103b0
Create Date: 2026-11-02 21:47:18.789613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19dfde2f1dc3'
down_revision: Union[str, Sequence[str], None] = '8c912e6103b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
