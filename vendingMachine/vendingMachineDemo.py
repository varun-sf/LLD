from inventory import Inventory
from product import Product
from vendingMachine import VendingMachine

class VendingMachineDemo:
    @staticmethod
    def run():
        inventory = Inventory()
        lays = Product("Lays", 5)
        snickers = Product("Snickers", 10)
        diarymilk = Product("Diarymilk",15)
        inventory.add_product(lays,5)
        inventory.add_product(snickers,5)
        inventory.add_product(diarymilk,10)
        print(inventory.get_all())
        vm = VendingMachine(inventory)
        vm.get_product(lays, 2)
        vm.insert_money(10)
        vm.get_product(lays, 1)
        vm.cancel()
        vm1 = VendingMachine(inventory)
        print(vm==vm1)


if __name__=="__main__":
    VendingMachineDemo.run()