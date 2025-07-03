from environment import Environment


class Mission:
    def __init__(self,x:int,y:int,env:Environment,capacity=2.0):
        if(env.is_clear(x,y)==False):
            raise ValueError("Position is incorrect!")
        self.x=x
        self.y=y
        self.capacity=capacity
        env.set_field(x,y,Environment.State.TARGET)
    