from environment import Environment
from mission import Mission
from drone import Drone
from scheduler import Scheduler
from mission import Mission
from mission import Charging_Mission

BATTERY_USAGE_PER_STEP = 3.0
BATTERY_USAGE_PER_STAY = 1.0

class FleetController:
    def __init__(self,env:Environment,missions:
                 list[tuple[Mission,Scheduler.Priority]],drones:list[Drone]):
        
        self.env=env
        self.schedule=Scheduler()
        self.drones=drones
        for mission,priority in missions:
            self.schedule.schedule_task(mission,priority)
        self.dispatch()

    def dispatch(self):
        mission=None
        for pr in Scheduler.Priority:
            bucket=self.schedule.tasks.get(pr,[])
            while bucket:
                idle=None
                idle=next((d for d in self.drones if(d.state==Drone.State.READY and mission==None)),None)
                if(idle==None):
                    return
                mission=bucket.pop()
                idle.assign_mission(self.env,mission)
                mission=None

    def step(self):

        for drone in self.drones:

            if drone.mission!=None: #DRONE has a mission
                x,y=drone.steps[0]
                if(self.env.get_field(x,y)==Environment.State.EMPTY or
                   self.env.get_field(x,y)==Environment.State.TARGET or
                   drone.battery>=BATTERY_USAGE_PER_STEP):
                    self.env.set_field(drone.x,drone.y,Environment.State.EMPTY)
                    self.env.set_field(x,y,Environment.State.DRONE)
                    drone.x=x
                    drone.y=y
                    drone.steps=drone.steps[1:]
                    drone.battery-=BATTERY_USAGE_PER_STEP
                if(drone.mission.x==drone.x and drone.mission.y==drone.y):
                    drone.mission_completion()

            else: #DRONE does not have a mission
                if(drone.battery>=BATTERY_USAGE_PER_STAY):
                    drone.battery-=BATTERY_USAGE_PER_STAY
                if(drone.battery<40):
                    if(Environment.find_charge(self.env,drone.x,drone.y)==None or
                       drone.battery<=BATTERY_USAGE_PER_STEP):
                        drone.state=Drone.State.BROKEN
                        continue
                    (x_charge,y_charge)=Environment.find_charge(self.env,drone.x,drone.y)
                    mission=Charging_Mission(x_charge,y_charge,self.env)
                    drone.assign_mission(self.env,mission)
        self.dispatch()