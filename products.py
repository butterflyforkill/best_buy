class Product:
    """
    A class representing a product in inventory.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.
        active (bool): The status of the product (active or inactive).

    Methods:
        __init__: Initializes the product with a name, price, and quantity.
        is_active: Returns whether the product is currently active.
        activate: Activates the product.
        deactivate: Deactivates the product.
        get_quantity: Returns the current quantity of the product.
        set_quantity: Sets the quantity of the product.
        show: Returns a string representing the product details.
        buy: Buys a given quantity of the product
            and returns the total price of the purchase.

    """
    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method.

        Creates the instance variables (active is set to True).

        If something is invalid (empty name / negative price or quantity),
        raises an exception.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item.

        Raises:
            ValueError: If the name is empty
            or if the price or quantity is negative.
        """
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None


    def is_active(self) -> bool:
        """
        Returns whether the product is currently active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active


    def activate(self):
        """
        Activates the product, setting its active status to True.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product,
        setting its active status to False.
        """
        self.active = False


    def get_quantity(self) -> float:
        """
        Returns the quantity of the product.

        Returns:
            float: The quantity of the product.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Sets the quantity of the product to the specified amount.
        If the quantity becomes zero, the product is deactivated.

        Args:
            quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def show(self) -> str:
        """
        Returns a string representing the product details.

        Returns:
            str: A string containing the name,
                price, and quantity of the product.
        """
        product_info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if self.promotion:
            product_info += f", Promotion: {self.promotion.name}"
        return product_info


    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.

        Returns the total price (float) of the purchase.

        Updates the quantity of the product.

        Args:
            quantity (int): The quantity of the product to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity to buy is not a positive integer.
            Exception: If there is not enough quantity available to buy.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to buy must be a positive integer")

        if quantity > self.quantity:
            raise Exception("Not enough quantity available to buy")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price
    
    def get_promotion(self) -> any:
        """
        Returns the promotion applied to the product.

        Returns:
            PromotionInterface: The promotion applied to the product, or None if no promotion is applied.
        """
        return self.promotion

    def set_promotion(self, promotion: any):
        """
        Sets the promotion applied to the product.

        Args:
            promotion (PromotionInterface): The promotion to apply to the product.
        """
        self.promotion = promotion


class NonStockedProduct(Product):
    """
    A subclass of Product representing a product that is not stocked.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.

    Methods:
        __init__: Initializes a NonStockedProduct with a name and price.
        show: Displays the product information and indicates that it is a non-stocked product.
    """
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        super().show()
        print("This is a non-stocked product")


class LimitedProduct(Product):
    """
    A subclass of Product representing a product with a limited quantity.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        max_quantity (int): The maximum allowed quantity of the product.

    Methods:
        __init__: Initializes a LimitedProduct with a name, price, and maximum quantity.
        buy: Buys a given quantity of the product, ensuring it doesn't exceed the maximum allowed quantity.
        show: Displays the product information and the maximum allowed quantity.
    """
    def __init__(self, name, price, quantity,  maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError("Quantity exceeds the maximum allowed quantity for this product")
        else:
            self.quantity -= quantity

    def show(self):
        super().show()
        print(f"Maximum Allowed Quantity: {self.max_quantity}")
