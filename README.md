# 🚀 Rocket Flight Simulator
A physics-based rocket launch simulator written in Python.
This program simulates a rocket launch by calculating thrust, gravity, fuel burn, velocity, and altitude over time.
## Features
- Dynamic rocket mass as fuel burns
- Thrust vs gravity calculations
- Powered flight phase
- Coasting phase after fuel depletion
- Detects when the rocket reaches space (100 km)
- Tracks maximum altitude and velocity
- Interactive menu system
- Replay option
- Input validation
## How It Works
The simulator calculates acceleration using:
Thrust / Mass
Then subtracts gravity to determine the rocket's net acceleration.
Fuel mass decreases every second, which changes the rocket's total mass and acceleration.
The simulation continues until the rocket returns to the ground.
## How to Run
1. Install Python (3.14)
2. Download this repository
3. Run the program
## Future Improvements
- Atmospheric drag
- Planet selection (Earth, Moon, Mars)
- Escape velocity detection
- Altitude graphs
- Rocket presets
## Author
Created by **Mink**
