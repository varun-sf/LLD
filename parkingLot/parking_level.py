from parking_spot import ParkingSpot
from vehicle import Vehicle
from account import Account
class ParkingLevel:
    def __init__(self, level_num, capacity):
        self.level_num = level_num
        self.capacity = capacity
        self.spots : list[ParkingSpot] = [ParkingSpot(i) for i in range(0, capacity) ]
    
    def set_park_vehicle(self, account: Account) -> bool:
        for spot in self.spots:
            if spot.get_availability():
                spot.set_vehicle(account)
                return True
        return False
    
    def unpark_vehicle(self, vehicle_no) -> bool:
        for spot in self.spots:
            if spot.get_vehicle() == vehicle_no:
                return spot.remove_vehicle()
        
               
    def get_level(self):
        print(f"level {self.level_num}")
        for spot in self.spots:
            print(spot.get_vehicle(),end=" ")
        print()

       

    