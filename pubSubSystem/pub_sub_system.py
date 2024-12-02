from concurrent.futures import ThreadPoolExecutor
from topics import Topic
from publisher import Publisher
class PubSubSystem:
    def __init__(self):
        self.topics = {}
        self.executor_service = ThreadPoolExecutor(max_workers=10)

    def create_topic(self, topic):
        self.topics.setdefault(topic, Topic(topic))
    
    def publish(self, publisher, message ):
        self.executor_service.submit(publisher.publish, message)
    
    def create_publisher(self, publisher, topic):
        topic_obj = self.topics.get(topic, None)
        if topic_obj:
            obj = Publisher(publisher, topic_obj)
            return obj
        print("error")

    def subscribe(self, subscriber, topic):
        topic_obj = self.topics.get(topic, None)
        if topic_obj:
            topic_obj.subscribe(subscriber)