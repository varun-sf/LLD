from road import Road
import time
class TrafficControlSystem:
    def  __init__(self):
        self.green_time = 30
        self.orange_time = 5
        self.roads  = []
        self.running = False

    def add_roads(self, road: Road):
        self.roads.append(road)
    
    def change_timer(self, green_time = None, orange_time = None):
        self.orange_time  = orange_time if orange_time else self.orange_time
        self.green_time = green_time if green_time else self.green_time

    def run(self, index = 0 ):
       total = len(self.roads)-1
       self.running = True

       while self.running:
           print(f"{self.roads[index].name}- green, rest- Red")
           time.sleep(self.green_time)
           nextIndex = index+1 if index+1<=total else 0
           print(f"{self.roads[index].name} and {self.roads[nextIndex].name}- orange, Rest-Red ")
           time.sleep(self.orange_time)
           index = nextIndex
    
    def stop(self):
        self.running = False

    def emergency(self, road: Road):
        self.stop()
        count = 0
        for i in self.roads:
            if i == road:
              break
            count+=1
        self.run(count)


           