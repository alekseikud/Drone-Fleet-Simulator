from environment import Environment
from mission import Mission
from drone import Drone
from scheduler import Scheduler
from mission import Mission


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
            if drone.mission!=None:
                x,y=drone.steps[0]
                if(self.env.get_field(x,y)==Environment.State.EMPTY or
                   self.env.get_field(x,y)==Environment.State.TARGET):
                    self.env.set_field(drone.x,drone.y,Environment.State.EMPTY)
                    self.env.set_field(x,y,Environment.State.DRONE)
                    drone.x=x
                    drone.y=y
                    drone.steps=drone.steps[1:]
                if(drone.mission.x==x and drone.mission.y==y):
                    drone.mission_completion()
        self.dispatch()