"""update model employee settings created_at & updated_at

Revision ID: aaee7ceea126
Revises: b1af3c7a56b3
Create Date: 2024-07-10 12:52:35.490609

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aaee7ceea126'
down_revision: Union[str, None] = 'b1af3c7a56b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
