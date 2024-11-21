# Vacuum-Cleaner-Simple-Reflex-Agent-
This project implements a simple vacuum cleaner simulation (A Simple Reflex AI Model). The vacuum cleaner operates in a two-room environment (`L` for Left, `R` for Right) and performs actions such as **SUCK** (cleaning the room) or moving between rooms (**MOVERIGHT** and **MOVELEFT**) based on the current state.


## Description

The vacuum cleaner's objective is to clean both rooms, starting from a given initial state. The program demonstrates how a simple agent can function in a two-room environment by:
1. Determining actions based on the current state.
2. Updating the state after performing an action.
3. Checking if all rooms are clean.

### Features:
- Simulation of vacuum cleaner actions.
- Clear logic to switch states and handle conditions for cleaning or movement.
- Handles two scenarios: starting in the **Right** room (`R`) or the **Left** room (`L`).
- Terminates gracefully if stuck in an infinite loop or upon completion.

## Explanation

The simulation has four main functions:

### 1. `getAction(state)`
Determines the next action the vacuum cleaner should take based on the current state:
- **SUCK**: Cleans the room if dirty.
- **MOVELEFT/MOVERIGHT**: Moves to the adjacent room if the current room is clean.
- **None**: Stops if no valid action is found.

### 2. `updateState(state, action)`
Updates the vacuum cleaner's state based on its action:
- If cleaning (`SUCK`), the room is marked clean (`0`).
- If moving (`MOVELEFT`/`MOVERIGHT`), the vacuum cleaner's position is updated.

### 3. `bool_all_rooms_clean(state)`
Checks if all rooms are clean:
- Returns `True` if both rooms are clean (`[0, 0]`).
- Returns `False` otherwise.

### 4. `run_vacuum(start_state)`
Runs the simulation:
- Repeatedly determines the action using `getAction`.
- Updates the state using `updateState`.
- Stops when all rooms are clean or if the program enters too many cycles, indicating a potential bug.

### Example Outputs:
#### Start in Room `R`:

```
Start State: ['R', [1, 1]] cycle:0 action=SUCK
state=['R', [1, 0]] cycle:1 action=MOVELEFT
state=['L', [1, 0]] cycle:2 action=SUCK
state=['L', [0, 0]] All rooms clean!

shell
Copy code
```

#### Start in Room `L`:
```
Start State: ['L', [1, 1]] cycle:0 action=SUCK
state=['L', [0, 1]] cycle:1 action=MOVERIGHT
state=['R', [0, 1]] cycle:2 action=SUCK
state=['R', [0, 0]] All rooms clean!
```
## How to Run the Program

### Prerequisites
- Python 3.x installed on your system.

### Steps:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/vacuum-cleaner-simulation.git
   cd vacuum-cleaner-simulation
   ```
2. Run the script:
   ```
   python vacuum_cleaner.py
   ```

3. View the simulation outputs in the terminal for both scenarios:
   - Starting in room `R`.
   -  Starting in room `L`.

##Expected Output
The program will display step-by-step actions of the vacuum cleaner, followed by the state changes. Once both rooms are clean, it will print All rooms clean!.

.
├── vacuum_cleaner.py   # Main Python script
└── README.md           # Project documentation
.

