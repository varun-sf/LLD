from parking_lot import ParkingLot
from vehicle import Vehicle
from account import Account

class ParkingSystem:
    _instance = None
    def __init__(self):
        if ParkingSystem._instance is not None:
            raise Exception("Already object exists")
        ParkingSystem._instance = self
        self.parking_lot = ParkingLot()

    @staticmethod
    def get_instance():
        if ParkingSystem._instance is None:
            ParkingSystem._instance = ParkingSystem()
        return ParkingSystem._instance
    
    def add_level(self, num, capacity):
        self.parking_lot.add_level(num,capacity)
    
    def set_park_vehicle(self, vehicle: Vehicle)-> bool:
        # Create account
        account = Account(vehicle)
        return self.parking_lot.set_park_vehicle(account)
    
    def unpark_vehicle(self, vehicle_no):
        return self.parking_lot.unpark_vehicle(vehicle_no)
    
    def display_spots(self):
        self.parking_lot.display_spots()
    
