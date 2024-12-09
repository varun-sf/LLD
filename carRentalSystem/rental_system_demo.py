from rental_system import RentalSystem
from car import Car
import time
class RentalSystemDemo:
    @staticmethod
    def run():
        system = RentalSystem()
        car1 = Car("Toyota", "Camry", 2015, 100000, 5000)
        system.add_car(car1)
        system.register_customer("Varun",8247757527,"apwei2i2")
        system.get_cars()
        time.sleep(2)
        system.make_reservation(car1, 8247757527)
        time.sleep(2)
        system.end_reservation(car1)

if __name__ =="__main__":
 RentalSystemDemo.run()
