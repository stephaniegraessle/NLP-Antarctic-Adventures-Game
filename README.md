# NLP-Antarctic-Adventures-Game

Antarctic Adventures is an adventure exploration game featuring the player as a penguin in Antarctica. The game was created using [Python](https://www.python.org/) and [Grammatical Framework](https://www.grammaticalframework.org/). By typing commands into the chat system, the games uses utilizing natural language processing (NLP) to parse and carry out different command sentences, such as picking up and eating fish and other items and exploring around in the game map.

## Installation (Linux)

Note: If your operating system is Windows, install and use [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install).

1. Clone the repository in the target file location.
2. Run updates on the Linux machine with `sudo apt update && upgrade`.
3. Install Python with `sudo apt install python3 python3-pip ipython3 `.
4. Install PGF for Python with `pip install pgf`.
5. Run the program with `python3 main.py`.

## User guide

### Player needs
You start with MAX_HUNGER and MAX_HP. Each turn, hunger decreases by NORMAL_HUNGER_LOSS_RATE until reaching 0. Eating food will increase the hunger by FOOD_HUNGER_GAIN_RATE. If hunger reaches 0, the HP will decrease each turn by STARVING_HP_LOSS_RATE. If HP reaches 0, the game ends.
|Stat|Amount|Ways to decrease|Ways to increase|
|---|---|---|---|
|Hunger|0-MAX_HUNGER|-NORMAL_HUNGER_LOSS_RATE each turn|+FOOD_HUNGER_GAIN_RATE when eating food|
|HP|0-MAX_HP|-STARVING_HP_LOSS_RATE each turn when Hunger is at 0|+FOOD_HP_GAIN_RATE when eating food|

These constant values can be modified in constant.py.

#### Foods
Currently, the only food in the game is fish, which you can find in the ocean environment.

### Navigation
You start at location (0,0), and can command to move in the cardinal directions North, East, West, or South to explore different areas. When moving locations, the program generates a new environment with different items in it. Use this feature to catch fish to eat.

## Change log
### 10 March, 2024
- Program states player location, generated environment, and inventory contents
- With commands, player can:
  - Pick up items to add to inventory
  - Drop items, removing them from inventory and placing them back in environment
  - Eat fish, removing them from inventory and increasing hunger
  - Move to a different location
- Player dies if HP becomes 0 from hunger loss

## Known Issues
- Program generates environments ever time the player moves--does not have a 'map' of the environment to remember where places and things are
