from datetime import datetime
import math

class Payment:  
    @staticmethod 
    def get_amount(price, time):
        current_time = datetime.now()
        difference = current_time - time
        return price * (math.ceil(difference.total_seconds()/3600))