from coffee  import Coffee
class Payment():
    def __init__(self, coffee:  Coffee):
        self.coffee = coffee
        
    
    def make_payment(self, payment : float):
        if payment >= self.coffee.price:
            print(f"payment is successfull, pls collect {payment-self.coffee.price}")
            return True
        
        print("Insufficient funds")
        return  False

