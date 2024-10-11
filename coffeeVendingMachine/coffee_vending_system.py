from expresso import Expresso
from cappacino import  Cappacino
from latte import Latte
from coffeesystem import coffeesystem

class CoffeeVendingMachine:
    @staticmethod
    def run():
        expresso = Expresso("expresso", 5)
        vending_machine = coffeesystem(100,100,100)
        vending_machine.get_ingredients()
        vending_machine.make_coffee(expresso, 1)
        vending_machine.make_coffee(expresso,20)
        vending_machine.make_coffee(expresso, 10)
        vending_machine.make_coffee(expresso, 10)


if  __name__ == "__main__":
    CoffeeVendingMachine.run()
