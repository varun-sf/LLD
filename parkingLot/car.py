from vehicle import Vehicle
from vehicle_type import VehicleType

class Car(Vehicle):
    def __init__(self, vehicle_no):
       
        super().__init__(licence_no= vehicle_no, vehicle_type= VehicleType.CAR)