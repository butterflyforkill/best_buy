import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotion import PromotionInterface, PercentageDiscount, FixedAmountDiscount, BuyOneGetOneFree


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


@pytest.mark.parametrize("purchase_quantity", [0, -1])
def test_purchase_with_invalid_quantity(purchase_quantity):
    """Tests buying a non-positive quantity of a product."""
    product = Product("Headset", 75.99, 10)
    with pytest.raises(ValueError):
        product.buy(purchase_quantity)


@pytest.mark.parametrize("initial_quantity, purchase_quantity", [(5, 7)])
def test_purchase_exceeds_available_quantity(initial_quantity, purchase_quantity):
    """Tests buying a quantity larger than the available stock."""
    product = Product("Webcam", 39.99, initial_quantity)
    with pytest.raises(Exception):
        product.buy(purchase_quantity)


# Test promotion-related functionality
def test_product_set_and_get_promotion():
    product = Product("Laptop", 999.99, 5)
    promotion = PercentageDiscount("Summer Sale", 10)

    product.set_promotion(promotion)
    assert product.get_promotion() == promotion


def test_product_buy_with_promotion():
    product = Product("Laptop", 999.99, 5)
    promotion = PercentageDiscount("Summer Sale", 10)
    product.set_promotion(promotion)

    total_price = product.buy(2)
    # Assert discounted price based on promotion logic
    assert total_price < (product.price * 2)  # Discounted price

@pytest.mark.usefixtures("mock_buy_for_non_stocked")
def test_promotion_applies_to_product_types(product_types):
    # Test promotion on different product types
    for product_type in product_types:
        if product_type == NonStockedProduct:
            product = product_type("Test Product", 100.00)
        elif product_type == LimitedProduct:
            product = product_type("Test Product", 100.00, 10, 20)
        else:  # Assuming Product
            product = product_type("Test Product", 100.00, 10)
        promotion = PercentageDiscount("Summer Sale", 10)
        product.set_promotion(promotion)

        total_price = product.buy(2)
        # Assert discounted price or None based on product type
        if isinstance(product, (NonStockedProduct, LimitedProduct)):
            assert total_price is None  # Promotion not applicable
        else:
            assert total_price < (product.price * 2)  # Discounted price


@pytest.fixture
def product_types():
    return [Product, NonStockedProduct, LimitedProduct]


@pytest.fixture
def mock_buy_for_non_stocked(mocker):
    mocker.patch.object(NonStockedProduct, "buy", return_value=None)