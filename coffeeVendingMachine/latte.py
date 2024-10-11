from coffee import  Coffee

class Latte(Coffee):
    def __init__(self, name, price):
        super().__init__(name, price, 50, 20, 100)