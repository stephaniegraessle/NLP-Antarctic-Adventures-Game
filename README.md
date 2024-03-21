# NLP-Antarctic-Adventures-Game

Antarctic Adventures is a text-based adventure exploration game featuring the player as a penguin in Antarctica. The game was created using [Python](https://www.python.org/) and [Grammatical Framework](https://www.grammaticalframework.org/). By typing commands into the chat system, the games uses utilizing natural language processing (NLP) to parse and carry out different command sentences, such as picking up and eating fish and other items and exploring around in the game map.

 **Table of contents**
 - [Files overview](#files-overview)
 - [Known issues](#known-issues)
 - [Change log](#change-log)
 - [Installation](#installation)
 - [User guide](#user-guide)
   - [Navigation](#navigation)
     - [Environments](#environments)
   - [Player needs](#player-needs)
     - [Foods](#foods)

<a id="files-overview"></a>
## Files overview
|File|Contents|
|---|---|
|Adventure.gf|abstract grammar|
|AdventureEng.gf|concrete grammar|
|constant.py|constants|
|event.py|functions for different user-specified commands|
|helper.py|functions helping to carry out miscellaneous tasks|
|main.py|main function|
|output.py|functions for outputting text to the user and logging|
|process.py|fuctions for parsing and processing inputted expressions|

<a id="known-issues"></a>
## Known Issues
- Program generates environments ever time the player moves--does not have a 'map' of the environment to remember where places and things are
- Game crashes when trying to pick up more object than there are on the ground--tell player also how many of an object they see on the ground.
- Add statements for hunger and health instead of numbers, show every few turns, not every turn.
- Show inventory only when player asks
- No statement for when trying to catch fish outside of ocean area/in a place where there is no fish

<a id="change-log"></a>
## Change log
### 10 March, 2024
- Program states player location, generated environment, and inventory contents
- With commands, player can:
  - Pick up items to add to inventory
  - Drop items, removing them from inventory and placing them back in environment
  - Eat fish, removing them from inventory and increasing hunger
  - Move to a different location
- Player dies if HP becomes 0 from hunger loss

<a id="installation"></a>
## Installation (Linux)
Note: These commands only run on Linux. If your operating system is Windows, you can install and use [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install).

1. Clone the repository in the target file location.
2. Run updates on the Linux machine with `sudo apt update && upgrade`.
3. Install Python with `sudo apt install python3 python3-pip ipython3 `.
4. Install PGF for Python with `pip install pgf`.
5. Run the program with `python3 main.py`.

<a id="user-guide"></a>
## User guide

<a id="navigation"></a>
### Navigation
You start at location (0,0), and can command to move in the cardinal directions North, East, West, or South to explore different areas. When moving locations, the program generates a new environment with different items in it. Use this feature to catch fish to eat.

<a id="environments"></a>
#### Environments
Certain items generate in each environment.
|Environment|Possible items|
|---|---|
|Ocean|Fish|
|Snow field|Ice, Rock, Snow|

<a id="player-needs"></a>
### Player needs
You start with MAX_HUNGER and MAX_HP. Each turn, hunger decreases by NORMAL_HUNGER_LOSS_RATE until reaching 0. Eating food will increase the hunger by FOOD_HUNGER_GAIN_RATE. If hunger reaches 0, the HP will decrease each turn by STARVING_HP_LOSS_RATE. If HP reaches 0, the game ends.
|Stat|Amount|Ways to decrease|Ways to increase|
|---|---|---|---|
|Hunger|0 - MAX_HUNGER|Decreases by NORMAL_HUNGER_LOSS_RATE each turn|Increases by FOOD_HUNGER_GAIN_RATE when eating food|
|HP|0 - MAX_HP|Decreases by STARVING_HP_LOSS_RATE each turn when Hunger is at 0|Increases by FOOD_HP_GAIN_RATE when eating food|

\* You can modify these constant values in constant.py.

<a id="foods"></a>
#### Foods
|Food|Environment|
|---|---|
|Fish|Ocean|
