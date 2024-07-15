from products import Product


class Store:
    """
    A class representing a store that holds
    a collection of products and provides operations
    to manage and retrieve product information.

    Attributes:
    - products (list): A list of Product objects representing
                the products available in the store.

    Methods:
    - __init__(self, products=None): Initializes the Store with a list of products.
        If no products are provided, an empty list is created.
    - add_product(self, product): Adds a new product to the store's product list.
    - remove_product(self, product): Removes a specified product
        from the store's product list.
    - get_total_quantity(self) -> int: Calculates and returns the total quantity
        of all products in the store.
    - get_all_products(self) -> list[Product]: Retrieves a list of all
        active products available in the store.
    - order(self, shopping_list) -> float: Processes an order based
        on a given shopping list and returns the total price of the order.
    """
    def __init__(self, products=None):
        """
        Initializes the Store with a list of products.
        If no products are provided, an empty list is created.

        Args:
        - products (list, optional): A list of Product objects
        representing the initial products available in the store.
        Defaults to None.
        """
        self.products = products if products is not None else []

    def add_product(self, product):
        """
        Adds a new product to the store's product list.

        Args:
        - product (Product): The Product object to be added to the store.

        Returns:
        None
        """

        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a specified product from the store's product list.

        Args:
        - product (Product): The Product object
        to be removed from the store.

        Returns:
        None
        """
        index = self.products.index(product)
        del self.products[index]

    def get_total_quantity(self) -> int:
        """
        Calculates and returns the total quantity
        of all products in the store.

        Returns:
        int: The total quantity of all products in the store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> list[Product]:
        """
        Retrieves a list of all active products available in the store.

        Returns:
        list[Product]: A list of all active products
            available in the store.
        """
        products_list_active = []
        for product in self.products:
            if product.active is True:
                products_list_active.append(product)
        return products_list_active

def order(shopping_list) -> float:
    """
    Processes an order based on a given shopping
    list and returns the total price of the order.

    Args:
    - shopping_list (list): A list of tuples
        representing the products and quantities to be ordered.

    Returns:
    float: The total price of the order.
    """
    total_price = 0
    for product, quantity in shopping_list:
        total_price += product.buy(quantity)
    return total_price
