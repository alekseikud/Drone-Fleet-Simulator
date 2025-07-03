# Drone Fleet Simulator

A Python-based autonomous drone fleet simulation that demonstrates pluggable scheduling policies and path-planning strategies on a grid environment with obstacles and charging stations.

## Features

* **Environment Loading**: Read grid maps from JSON files.
* **Mission Management**: Create and assign missions with pickup/drop-off points, deadlines, and payload capacities.
* **Path Planning**: Plug-in routing strategies (BFS) for path computation.
* **Scheduling**: FIFO, priority-queue modes via a flexible `Scheduler` interface.
* **Controller**: `FleetController` orchestrates environment, drones, missions, and logs KPIs.
* **Visualization**: Console rendering of the grid with Unicode symbols.

## Repository Name

**`drone-fleet-sim`**

## Description

Simulate an autonomous fleet of drones operating in a 2D grid environment with obstacles and charging stations. This project showcases software design patterns like the Strategy and Factory patterns, and emphasizes clean separation of concerns.

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/drone-fleet-sim.git
   cd drone-fleet-sim
   ```
2. Prepare a map JSON in `parameters.json`, or use one of the provided example files.

### Usage

Run the main script:

```bash
python main.py
```

## Project Structure

```
├── environment.py       # Environment and map loading
├── mission.py           # Mission class (immutable)
├── drone.py             # Drone class with state and behaviors
├── scheduler.py         # Task scheduling policies
├── routing_strategy.py  # Abstract and concrete path planners
├── fleet_controller.py  # Simulation orchestrator
├── main.py              # Example usage and simulation loop
├── parameters.json      # Example map files
└── README.md            # This file
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to add new scheduling strategies, routing algorithms, or visualization options.

## License

This project is released under the **MIT License**—a permissive, business-friendly license that allows reuse, distribution, and private modification. See [LICENSE](LICENSE) for full details.
