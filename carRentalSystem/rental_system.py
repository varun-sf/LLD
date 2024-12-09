from reservation import Reservation
from customer import Customer
from payment import Payment

class RentalSystem:
    def __init__(self):
        self.cars = {}
        self.customers = {}

    def add_car(self, car):
        if car not in self.cars:
            self.cars[car] = None
    
    def get_cars(self, all=False):
        for car, reservation in self.cars.items():
            if not all and reservation:
                car.get_details()
                continue
            car.get_details()
            print("-- Available")

    
    def make_reservation(self, car, customer_no):
        if not car and self.cars[car]:
            print("Invalid car or not available")
            return
        if customer_no not in self.customers:
            print("Please register customer")
            return 
        self.cars[car] = Reservation(self.customers[customer_no])

    
    def register_customer(self, name, contact_details, driver_license):
        self.customers[contact_details] = Customer(name, contact_details, driver_license)

    def end_reservation(self, car):
        print(Payment.get_amount(car.price, self.cars[car].starttime))


    