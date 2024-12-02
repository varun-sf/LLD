from pub_sub_system import PubSubSystem
from subscriber import Subscriber
from publisher import Publisher
class PubSubSystemDemo:
    @staticmethod
    def run():
        # Create a PubSubSystem instance
        pubsub = PubSubSystem()
        pubsub.create_topic("sport1")
        publisher1 = pubsub.create_publisher("manas","sport1")
      
       
        pubsub.subscribe(Subscriber("varun"),"sport1")
        pubsub.subscribe(Subscriber("name"),"sport1")
        pubsub.publish(publisher1, "Hello, world!")

if __name__ == "__main__":
    PubSubSystemDemo.run()

        