from abc import ABC, abstractmethod
from products import Product, NonStockedProduct, LimitedProduct

class PromotionInterface(ABC):
    """
    Abstract class representing a promotion.

    Attributes:
        name (str): The name of the promotion.

    Methods:
        apply_promotion(product, quantity) -> float:
            Applies the promotion to a product and returns the discounted price.
    """
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Applies the promotion to 
        a product and returns the discounted price.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product being purchased.

        Returns:
            float: The discounted price after applying the promotion.
        """
        pass


class PercentageDiscount(PromotionInterface):
    """
    A promotion that offers a percentage discount on a product.

    Attributes:
        discount_percentage (float): The percentage discount to apply.
    """
    def __init__(self, name, discount_percentage):
        super().__init__(name)
        self.discount_percentage = discount_percentage
    
    def apply_promotion(self, product: Product, quantity: int) -> float:
        if isinstance(product, (NonStockedProduct, LimitedProduct)):
            return None
        original_price = product.price * quantity
        discount_amount = original_price * (self.discount_percentage / 100)
        return original_price - discount_amount


class FixedAmountDiscount(PromotionInterface):
    """
    A promotion that offers a fixed amount discount on a product.

    Attributes:
        discount_amount (float): The fixed amount discount to apply.
    """
    def __init__(self, name, discount_amount):
        super().__init__(name)
        self.discount_amount = discount_amount
    
    def apply_promotion(self, product: Product, quantity: int) -> float:
        if isinstance(product, (NonStockedProduct, LimitedProduct)):
            return None
        original_price = product.price * quantity
        return original_price - self.discount_amount


class BuyOneGetOneFree(PromotionInterface):
    """
    A promotion that offers a "buy one, get one free" deal on a product.
    """
    def apply_promotion(self, product: Product, quantity: int) -> float:
        if isinstance(product, (NonStockedProduct, LimitedProduct)):
            return None
        original_price = product.price * quantity
        return original_price // 2
    
        