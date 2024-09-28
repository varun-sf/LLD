from account import Account
  
class ParkingSpot:
    def __init__(self, id):
        self.spot_number = id
        self.parked_account = None

    def get_availability(self):
        return self.parked_account==None
    
    def set_vehicle(self, account: Account):
        self.parked_account = account
    
    def get_vehicle(self):
        if self.parked_account==None:
            return "Empty"
        
        return self.parked_account.get_account()
    
    def remove_vehicle(self):
        ans = self.parked_account.end_account()
        self.parked_account = None
        return ans