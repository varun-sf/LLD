# Each car should have details such as make, model, year, license plate number, and rental price per day.

class Car:
    def __init__(self, make, model, year, license_plate_number, rental_price):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate_number = license_plate_number
        self.price = rental_price
    
    def get_details(self):
        print(f"Car of {self.make} {self.model}- {self.year} with license no- {self.license_plate_number} priced at {self.price}")