# import time

# from environment import Environment
# from mission import Mission
# from drone import Drone
# from scheduler import Scheduler
# from fleet_controller import FleetController

# def create_test_environment(path="parameters.json") -> Environment:
#     # Load the grid
#     return Environment.from_json(path)          # :contentReference[oaicite:0]{index=0}

# def create_test_missions(env: Environment):
#     # Missions are (x, y, env) → capacity default 2.0
#     # Pair each with a Scheduler.Priority
#     return [
#         (Mission(2, 0, env), Scheduler.Priority.HIGH),    # clear cell :contentReference[oaicite:1]{index=1}
#         (Mission(4, 3, env), Scheduler.Priority.MEDIUM),
#     ]

# def create_test_drones(env: Environment):
#     # Spawn two drones at READY positions
#     # __init__ signature: Drone(x:int, y:int, env:Environment, …)
#     return [
#         Drone(0, 0, env),    # top-left corner :contentReference[oaicite:2]{index=2}
#         Drone(1, 4, env),    # somewhere else
#     ]

# def main():
#     env     = create_test_environment()
#     missions= create_test_missions(env)
#     drones  = create_test_drones(env)

#     # Construct your controller (it auto-dispatches pending missions)
#     fc = FleetController(env, missions, drones)            # :contentReference[oaicite:3]{index=3}

#     steps = 10
#     for i in range(steps):
#         print(f"\n=== Step {i+1} ===")
#         # Print raw map (you could swap in your own render)
#         env.print_map()                                    # :contentReference[oaicite:4]{index=4}
#         # Advance one tick
#         fc.step()
#         time.sleep(0.5)

# if __name__ == "__main__":
#     main()

# main.py
# main.py
import time
import random
import subprocess

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
    for step in range(1, 11):
        subprocess.run(['clear']) 
        print(f"\n=== Step {step} ===")
        env.print_map()      # your built-in map printer
        controller.step()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
