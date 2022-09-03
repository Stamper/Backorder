import pytest
from freezegun import freeze_time

from orders.models import Product


@pytest.fixture
def product(db):
    return Product.objects.create(title="Test Product", price=99.99)


@pytest.fixture
def product_discount(db):
    with freeze_time("2022-01-01"):
        return Product.objects.create(title="Discount Product", price=100)
