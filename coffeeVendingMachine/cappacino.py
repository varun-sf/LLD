from coffee import  Coffee

class Cappacino(Coffee):
    def __init__(self, name, price):
        super().__init__(name, price, 50, 20, 50)