from vehicle import Vehicle
from datetime import datetime

class Account:
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.starttime = datetime.now()

    def get_account(self):
        return self.vehicle.get_vehicle_number()
    
    def end_account(self):
       end_time = datetime.now()
       total_time = end_time-self.starttime
       minutes = total_time.total_seconds()/60
       return minutes
  
