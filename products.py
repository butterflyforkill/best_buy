class Product:
    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method.
        
        Creates the instance variables (active is set to True).
        
        If something is invalid (empty name / negative price or quantity), raises an exception.
        
        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item.
            
        Raises:
            ValueError: If the name is empty or if the price or quantity is negative.
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
    
    
    def is_active(self) -> bool:
        return self.active
    
    
    def activate(self):
        self.active = True
    
    
    def deactivate(self):
        self.active = False
    
    
    def get_quantity(self) -> float:
        return self.quantity
    
    
    def set_quantity(self, quantity):
        self.quantity = quantity 
        if self.quantity == 0:
            self.deactivate()
    
    
    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    
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
        
        total_price = self.price * quantity
        self.quantity -= quantity
        return total_price