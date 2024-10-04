from inventory import Inventory
from product import Product
from money import Money

class VendingMachine:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)       
        return cls._instance
    
    def __init__(self, inventory: Inventory):
        if not hasattr(self, 'initialized'):
            self.inventory = inventory
            self.money = 0
    
    def insert_money(self, money):
        checker = False
        for mon in Money:
            if money==mon.value:
                checker = True
                break
        if not checker:
            print("Invalid denomination entered")
            return

        self.money +=money
    
    def get_product(self, product: Product, quantity):
        stock = self.inventory.get_quantity(product)
        if quantity>stock:
           print(f"{quantity} is not available")
           return 
        if self.money< product.price*quantity:
           print(f"Add {product.price*quantity-self.money}rs more")
           return
        
        self.inventory.update_quantity(product,stock-quantity)
        print(f"{product.name} is dispensed of {quantity} quantity")
        self.money -= product.price*quantity
                
        
    def cancel(self):
        money = self.money
        self.money=0
        return money  