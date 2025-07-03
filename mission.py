from environment import Environment


class Mission:
    def __init__(self,x:int,y:int,env:Environment,capacity=2.0):
        if(env.is_clear(x,y)==False and env.get_field(x,y)!=Environment.State.CHARGING):
            raise ValueError("Position is incorrect!")
        self.x=x
        self.y=y
        self.capacity=capacity
        env.set_field(x,y,Environment.State.TARGET)
    
class Charging_Mission(Mission):
    def __init__(self,x:int,y:int,env:Environment):
        super().__init__(x,y,env,0)
        env.set_field(x,y,Environment.State.CHARGING)