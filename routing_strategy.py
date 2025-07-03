from environment import Environment
from mission import Mission
from drone import Drone
from enum import IntEnum
from mission import Charging_Mission

class RoutingStrategy:

    class Move(IntEnum):
        FRONT=0
        BACK=1
        LEFT=2
        RIGHT=3
        
    def plan_path(self,env:Environment,dr:Drone,mis:Mission)->list:
        result=list()

        x_source=dr.x
        y_source=dr.y
        x_target=mis.x
        y_target=mis.y

        predecessor={}
        visited=set()
        visited.add((x_source,y_source))
        initial_layer=[(x_source,y_source)]
        result=self.bfs_layer(env,initial_layer,x_target,y_target,visited,predecessor)

        if result is None:
            return []
        
        path=[]
        node=(x_target,y_target) 
        while True :
            path.append(node)
            if node==(x_source, y_source):
                break
            node=predecessor[node]
        path = list(reversed(path))
        return path[1:]
    
    def bfs_layer(self,env:Environment,current_layer:list,x_target:int,y_target:int,visited:set,predecessor: dict)->list:

        if not current_layer:
            return None
        
        for (x,y) in current_layer:
            if x==x_target and y==y_target:
                return (x,y)
        
        next_layer=[]
        for (x,y) in current_layer:
            for(ny,nx) in Environment.get_neighbours(env,x,y):
                if(Environment.is_clear(env,nx,ny) and not ((nx,ny) in visited)):
                    visited.add((nx,ny))
                    predecessor[(nx,ny)]=(x,y)
                    next_layer.append((nx,ny))
        return self.bfs_layer(env,next_layer,x_target,y_target,visited,predecessor)