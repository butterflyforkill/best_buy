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


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store(product_list)
products = store.get_all_products()
for product in products: 
    print(product.name, product.price)
    print()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))