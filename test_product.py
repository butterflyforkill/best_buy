import pytest
from products import Product


@pytest.mark.parametrize("name, price, quantity", [
    ("", 100.00, 10),
    ("Keyboard", -50.00, 100),
])
def test_create_product_with_invalid_details(name, price, quantity):
    with pytest.raises(ValueError):
        Product(name, price, quantity)


@pytest.mark.parametrize("name, price, quantity", [
    ("Mouse", 25.00, 50),
    ("Monitor", 199.99, 20),
])
def test_create_product(name, price, quantity):
    product = Product(name, price, quantity)
    assert product.name == name
    assert product.price == price
    assert product.quantity == quantity


def test_product_becomes_inactive_at_zero_quantity():
    product = Product("Keyboard", 50.00, 3)

    for _ in range(3):
        product.buy(1)

    assert not product.is_active()


@pytest.mark.parametrize("initial_quantity, purchased_quantity, expected_remaining_quantity", [
    (10, 3, 7),  # Test case 1: Purchase 3 units from an initial quantity of 10
    (20, 5, 15),  # Test case 2: Purchase 5 units from an initial quantity of 20
    (15, 10, 5),  # Test case 3: Purchase 10 units from an initial quantity of 15
])
def test_product_purchase_modifies_quantity_and_returns_correct_output(initial_quantity, purchased_quantity, expected_remaining_quantity):
    # Arrange
    product = Product("Mouse", 25.00, initial_quantity)
    
    # Act
    initial_quantity = product.get_quantity()
    product.buy(purchased_quantity)
    remaining_quantity = product.get_quantity()
    
    # Assert
    assert remaining_quantity == initial_quantity - purchased_quantity
    assert remaining_quantity == expected_remaining_quantity    