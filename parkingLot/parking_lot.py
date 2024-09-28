from parking_level import ParkingLevel
from account import Account

class ParkingLot:
    
    def __init__(self):
            self.levels : list[ParkingLevel] = []
    
    def add_level(self, num, capacity):
        self.levels.append(ParkingLevel(num, capacity))

    def set_park_vehicle(self, account: Account):
        for level in self.levels:
            if level.set_park_vehicle(account):
                return True
        return False
    
    def unpark_vehicle(self, vehicle_no):

        for level in self.levels:
            ans = level.unpark_vehicle(vehicle_no)
            if ans:
                return ans
                
        
    
    def display_spots(self):
        for level in self.levels:
            
            level.get_level()
    