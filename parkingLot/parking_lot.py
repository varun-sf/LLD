from parking_level import ParkingLevel
from vehicle import Vehicle

class ParkingLot:
    
    def __init__(self):
            self.levels : list[ParkingLevel] = []
    
    def add_level(self, num, capacity):
        self.levels.append(ParkingLevel(num, capacity))

    def set_park_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.set_park_vehicle(vehicle):
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False
    
    def display_spots(self):
        for level in self.levels:
            
            level.get_level()
    