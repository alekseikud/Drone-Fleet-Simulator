from environment import Environment
from mission import Mission
from enum import IntEnum
from mission import Mission
from drone import Drone
from collections import defaultdict


class Scheduler:
    class Priority(IntEnum):
        HIGH=0
        MEDIUM=1
        LOW=2

    def __init__(self):
        self.tasks=defaultdict(list)
    
    def schedule_task(self,task:Mission,prior=Priority.LOW):
        self.tasks[prior].append(task)

    def task_remove(self,task:Mission)->bool:
        for value in self.tasks.values():
            if task in value:
                value.remove(task)
                return True
        return False
    
    