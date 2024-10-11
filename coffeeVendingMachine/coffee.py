from ingeridents import Ingredients
class Coffee:
    def  __init__(self, name, price, water, beans,  milk):

        self.name = name
        self.price = price
        self.water  = water
        self.beans = beans
        self.milk =  milk
   
    def can_make(self, ingredients: Ingredients):
        return self.water <= ingredients.water and self.beans <= ingredients.beans and self.milk <= ingredients.milk
    

    def make(self,  ingredients: Ingredients):
        ingredients.use_ingredients(self.water, self.milk ,self.beans)
        print(f"Enjoy your {self.name}")


        
