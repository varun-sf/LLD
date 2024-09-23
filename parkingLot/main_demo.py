from parking_system import ParkingSystem
from car import Car
class Main():
    def run():
        parking = ParkingSystem()
        parking.add_level(1, 8)
        parking.add_level(3, 2)
      
        print(parking.set_park_vehicle(Car("123")))
        print(parking.set_park_vehicle(Car("1234")))
        print(parking.set_park_vehicle(Car("12345")))
        print(parking.set_park_vehicle(Car("123456")))
        print(parking.set_park_vehicle(Car("12345")))
        print(parking.set_park_vehicle(Car("12345")))
        print("-")
        parking.display_spots()
        print(parking.unpark_vehicle("123456"))
        parking.display_spots()

if __name__ =="__main__":
    Main.run()
        