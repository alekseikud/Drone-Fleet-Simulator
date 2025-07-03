import numpy as np
import json
from pathlib import Path
from collections import defaultdict
from enum import IntEnum

class Environment:

    class State(IntEnum):
        EMPTY   = 0 #⬜
        OBSTACLE= 1 #🧱
        CHARGING= 2 #🔋
        DRONE   = 3 #🚁
        TARGET  = 4 #🎁

    @classmethod
    def from_json(cls,path:str)->"Environment":
        # reading from the json file
        with Path(path).open("r",newline="") as file:
            payload=json.load(file)
            width=payload["width"]
            height=payload["height"]
            grid=payload["grid"]

            # checking if the parameters are correct
            if len(grid)!=height or width!=(sum(len(idx) for idx in grid)//height):
                raise ValueError("Incorrect matrix passed")
            
            #string the data
            obj=cls()
            obj.width=width
            obj.height=height
            obj.grid=np.asarray(grid,dtype=np.int8)
            return obj
        
    def is_clear(self,x:int,y:int)->bool:
        if (x<0 or y<0 or y>=self.height or x>=self.width) :
            return False
        if self.grid[y][x]==Environment.State.OBSTACLE:
            return False
        else :
            return True
    
    def get_neighbours(self,x:int,y:int)->defaultdict:

        neighbours = defaultdict(lambda: Environment.State.OBSTACLE)

        # --- front  (east) ---
        if x + 1 < self.width :
            neighbours[(y, x + 1)] = self.grid[y][x + 1]

        # --- back   (west) ---
        if x - 1 >= 0:
            neighbours[(y, x - 1)] = self.grid[y][x - 1]

        # --- right  (south) ---
        if y + 1 < self.height:
            neighbours[(y + 1, x)] = self.grid[y + 1][ x]

        # --- left   (north) ---
        if y - 1 >= 0:
            neighbours[(y - 1, x)] = self.grid[y - 1] [x]
        return neighbours

    def set_field(self,x:int,y:int,state:State)->bool:
        if x>=0 and y>=0 and x<self.width and y<self.height and state<len(Environment.State):
            self.grid[y][x]=state
        else:
            return False
        
    def get_field(self,x:int,y:int)->"Environment.State":
        if x>=0 and y>=0 and x<self.width and y<self.height :
            return self.grid[y][x]
        else:
            return None
    def print_map(self):

        for j in range(self.width):
            for i in range(self.height):
                field=self.get_field(i,j)

                if(field==Environment.State.CHARGING): 
                    print("🔋",end="")
                if(field==Environment.State.DRONE): 
                    print("🚁",end="")
                if(field==Environment.State.OBSTACLE): 
                    print("🧱",end="")
                if(field==Environment.State.EMPTY): 
                    print("⬜",end="")
                if(field==Environment.State.TARGET): 
                    print("🎁",end="")
                if(i==self.height-1):
                    print()