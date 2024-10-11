from ingeridents import Ingredients
from coffee import  Coffee
from payment import  Payment


class coffeesystem:
    def __init__(self, water,  milk, coffee_beans):
        self.ingredients = Ingredients(water,  milk, coffee_beans)
    
    def make_coffee(self, coffee:  Coffee,  amount: float):
        if coffee.can_make(self.ingredients):
         if Payment(coffee=coffee).make_payment(amount):
          coffee.make(self.ingredients)
        else:
           print("Insufficient ingredients")

    def get_ingredients(self):
        print(self.ingredients)
        
           
           


