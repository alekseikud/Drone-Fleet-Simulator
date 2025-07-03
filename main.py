import time
import random
import subprocess
import sys

from environment import Environment
from mission import Mission
from drone import Drone
from scheduler import Scheduler
from fleet_controller import FleetController

def main():
    # 1) Load your map
    env = Environment.from_json("parameters.json")

    # 2) Create missions with different priorities
    missions = [
        (Mission(3, 2, env), Scheduler.Priority.HIGH),
        (Mission(7, 5, env), Scheduler.Priority.MEDIUM),
        (Mission(1, 8, env), Scheduler.Priority.LOW),
        (Mission(19, 19, env), Scheduler.Priority.LOW),
        (Mission(12, 10, env), Scheduler.Priority.LOW),
    ]

    # 3) Spawn drones at free locations
    drones = [
        Drone(0, 0, env),
        Drone(5, 5, env),
        Drone(9, 9, env),
    ]

    # 4) Build the controller (it uses its internal routing strategy)
    controller = FleetController(env, missions, drones)

    # 5) Run 10 simulation steps, printing the map each time
    for step in range(1, 100):
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()
        # print(f"\n=== Step {step} ===")
        env.print_map()      # your built-in map printer
        controller.step()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
