class Topic:
    def __init__(self, name):
        self.name = name
        self.subscriber = set()
        
    def send_message(self,message):
        for subscriber in self.subscriber:
            subscriber.message(message)

    def subscribe(self, subscriber):
        self.subscriber.add(subscriber)
    
    def unsubscribe(self, subscriber):
        self.subscriber.remove(subscriber)
