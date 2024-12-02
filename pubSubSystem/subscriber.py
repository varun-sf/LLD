class Subscriber:
    def __init__(self,name):
        self.name = name
    
    def message(self,message):
        print(f"{self.name} received {message}")