# time customer
from datetime import datetime
class Reservation:
    def __init__(self, customer):
        self.customer = customer
        self.starttime = datetime.now()