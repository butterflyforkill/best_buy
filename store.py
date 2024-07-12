from products import Product


class Store:
    def __init__(self, products=None):
        self.products = products if products is not None else []
    
    
    def add_product(self, product):
        self.products.append(product)
    
        
    def remove_product(self, product):
        index = self.products(product)
        del self.products[index]
    
    
    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity
    

    def get_all_products(self) -> list[Product]:
        products_list_active = []
        for product in self.products:
            if product.active == True:
                products_list_active.append(product)
        return products_list_active
    
    
    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
