from abc import ABC
from vehicle_type import VehicleType

class Vehicle(ABC):
    
    def __init__(self, licence_no: str, vehicle_type: VehicleType):
        self.licence_plate = licence_no
        self.vehicle_type = vehicle_type

    def get_vehicle_number(self):
        return self.licence_plate
    
