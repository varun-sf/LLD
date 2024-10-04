from product import Product
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, quantity):
        self.products[product] = quantity

    def get_quantity(self, product: Product):
        return self.products.get(product,0)
    
    def get_all(self):
        temp_str = ""
        for key, value in self.products.items():
            temp_str+=f"{key.name}-{value} quantity\n"
        return temp_str
    
    def remove_product(self, product: Product):
        del self.products[product]

    def update_quantity(self, product: Product, quantity):
        self.products[product] = quantity