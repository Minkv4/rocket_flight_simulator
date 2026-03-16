# 🚀 Python Rocket Physics Simulator
A terminal-based rocket launch simulator written in **Python**.
The program simulates rocket launches using simplified physics including gravity, fuel consumption, and atmospheric drag.
Users can choose different planets and rockets, then watch the rocket launch, reach peak altitude, and fall back to the surface.
---
# 🌌 Features
* 🌍 **Planet Selection**
  * Mercury
  * Venus
  * Earth
  * Moon
  * Mars
  * Jupiter
  * Saturn
  * Uranus
  * Neptune
Each planet has different **gravity** and **atmospheric drag**, which changes how the rocket behaves.
---
* 🚀 **Rocket Selection**
  * Space Launch System (SLS)
  * Falcon 9
  * Saturn V
  * Starship
  * Custom rocket builder
Users can also create their own rocket by entering:
* rocket mass
* fuel mass
* thrust
* fuel burn rate
---
* ⚙️ **Physics Simulation**
  The simulator models:
* thrust-based acceleration
* changing mass as fuel burns
* gravitational pull of planets
* atmospheric drag
* coasting phase after fuel depletion
---
* 📊 **Live Telemetry**
  During flight the simulator displays:
* Time
* Velocity
* Altitude
* Remaining fuel
* Altitude progress bar
---
* 🌠 **Space Detection**
  The simulator detects when the rocket crosses the **Kármán line (100 km)** and announces when space is reached.
---
* 🛬 **Landing System**
  After the rocket falls back:
* Safe landing if velocity is low
* Crash if velocity is too high
---
* 🧪 **Mission Results**
  At the end of each mission the program shows:
* Maximum altitude
* Maximum velocity
* Total flight time
* Mission result (Success / Suborbital / Failed)
---
# ▶️ How to Run
1. Install Python
2. Download the project
3. Run the simulator
```bash
python rocket_simulator.py
```
---
# 🧠 Concepts Used
This project demonstrates:
* Python functions
* loops and conditionals
* input validation
* physics simulation
* terminal-based UI
* simple game mechanics
---
# 🔧 Future Improvements
Possible upgrades:
* multi-stage rockets
* atmospheric density changing with altitude
* orbital velocity detection
* mission history tracking
* graphical interface
* real rocket databases
---
# 📚 Learning Purpose
This project was created as a learning exercise while practicing **Python programming and physics simulation concepts**.
---
# 🚀 Author
Created by **Mink**.
