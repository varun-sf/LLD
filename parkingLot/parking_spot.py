from vehicle import Vehicle
  
class ParkingSpot:
    def __init__(self, id):
        self.spot_number = id
        self.parked_vehicle = None

    def get_availability(self):
        return self.parked_vehicle==None
    
    def set_vehicle(self, vehicle: Vehicle):
        self.parked_vehicle = vehicle
    
    def get_vehicle(self):
        if self.parked_vehicle==None:
            return "Empty"
        
        return self.parked_vehicle.get_vehicle_number()
    
    def remove_vehicle(self):
        self.parked_vehicle = None