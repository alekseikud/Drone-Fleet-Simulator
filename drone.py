from enum import IntEnum
from environment import Environment


class Drone:

    class State(IntEnum):
        READY=0
        IN_MISSION=1
        BROKEN=2
        LOWBATTARY=3

    def __init__(self,x:int,y:int,env:Environment,battery=100,capacity=2):
        if(env.is_clear(x,y)):
            self.x=x
            self.y=y
            env.set_field(x,y,Environment.State.DRONE)
        self.state=Drone.State.READY
        self.battery=battery
        self.capacity=capacity
        self.mission=None
        self.steps=[]

    def assign_mission(self,env:Environment,mis):
        from routing_strategy import RoutingStrategy
        from mission import Mission
        from mission import Charging_Mission
        if(mis.capacity>self.capacity):
            raise ValueError("Capacity exceed!")
        self.state=Drone.State.IN_MISSION
        self.capacity-=mis.capacity
        self.mission=mis
        a=RoutingStrategy()
        self.steps=a.plan_path(env,self,mis)

    def mission_completion(self):
        from mission import Charging_Mission
        if(self.mission.x!=self.x or self.mission.y!=self.y):
            raise ValueError("Mission is not completed. Target coordinate:"
            "({self.target_x},{self.target_y}), Drone coordinate: ({self.x},{self.y})")
        self.capacity+=self.mission.capacity
        self.mission=None
        self.steps=[]
        self.state=Drone.State.READY
        if isinstance(self.mission,Charging_Mission):
            self.battery=100
            