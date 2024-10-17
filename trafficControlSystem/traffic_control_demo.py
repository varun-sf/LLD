from trafficControlSystem.traffic_system import  TrafficControlSystem
from road import  Road


class TrafficControlDemo:
    @staticmethod
    def run():
        system =  TrafficControlSystem()
        system.add_roads(Road("A"))
        system.add_roads(Road("B"))
        system.add_roads(Road("C"))
        r1 = Road("D")
        system.add_roads(r1)
        system.run()
       
        system.emergency(r1)
        system.stop()

if __name__ =="__main__":
    TrafficControlDemo.run()