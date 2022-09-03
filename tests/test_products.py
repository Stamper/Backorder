def test_product(product):
    assert product.title == "Test Product"
    assert product.price == 99.99
    assert product.discount == 0


def test_discount(product_discount):
    assert product_discount.title == "Discount Product"
    assert product_discount.price == 100
    assert product_discount.discount == 20
