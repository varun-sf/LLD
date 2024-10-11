class Ingredients:
    def __init__(self,water,milk,beans):
        self.water = water
        self.milk  = milk
        self.beans = beans
    
    def use_ingredients(self, water, milk, beans):
        self.water -= water
        self.milk  -= milk
        self.beans -= beans
        
    def  __str__(self):
        return f"water: {self.water}, milk: {self.milk}, beans: {self.beans}"
    
    

    
    
