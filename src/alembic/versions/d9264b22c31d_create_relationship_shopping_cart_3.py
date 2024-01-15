"""create_relationship_shopping cart 3

Revision ID: d9264b22c31d
Revises: 6ee94a0eb310
Create Date: 2024-01-16 00:46:15.612869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9264b22c31d'
down_revision: Union[str, None] = '6ee94a0eb310'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'customers', ['id'])
    op.create_unique_constraint(None, 'departments', ['id'])
    op.create_unique_constraint(None, 'discounts', ['id'])
    op.create_unique_constraint(None, 'order_items', ['id'])
    op.create_unique_constraint(None, 'order_products', ['id'])
    op.create_unique_constraint(None, 'orders', ['id'])
    op.create_unique_constraint(None, 'product_categories', ['id'])
    op.create_unique_constraint(None, 'products', ['id'])
    op.create_unique_constraint(None, 'shopping_cart', ['id'])
    op.create_unique_constraint(None, 'shopping_cart_items', ['id'])
    op.create_unique_constraint(None, 'users', ['id'])
    op.create_unique_constraint(None, 'verification_tokens', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'verification_tokens', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'shopping_cart_items', type_='unique')
    op.drop_constraint(None, 'shopping_cart', type_='unique')
    op.drop_constraint(None, 'products', type_='unique')
    op.drop_constraint(None, 'product_categories', type_='unique')
    op.drop_constraint(None, 'orders', type_='unique')
    op.drop_constraint(None, 'order_products', type_='unique')
    op.drop_constraint(None, 'order_items', type_='unique')
    op.drop_constraint(None, 'discounts', type_='unique')
    op.drop_constraint(None, 'departments', type_='unique')
    op.drop_constraint(None, 'customers', type_='unique')
    # ### end Alembic commands ###
