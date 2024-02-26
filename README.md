# NLP-Antarctic-Adventures-Game

Utilizes GF and Python to create a adventure exploration game incorporating natural language processing.

## Installation (Linux)

Note: If your machine is not Linux, install and use [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install).

1. Clone repository.
2. Download and [Grammatical Framework](https://www.grammaticalframework.org/download/index-3.11.html).
3. Run updates with `sudo apt update && upgrade`.
4. Install Python with `sudo apt install python3 python3-pip ipython3 `.
5. Install PGF with `pip install pgf`.
6. Run program with `python3 Adventure.py`.

## Change log

## Known Issues
- Grammar does not parse or generete sentences in past tense, only present tense

## Proposal

This is a basic adventure exploration chat system game created using GF and Python. In the game, the user is a penguin exploring around the Antactic. The penguin can complete different actions such as swimming in lakes or eating, and move around to different places. To incorporate the use of a data structure, I will use a list to have an "inventory" within which the penguin can pick up store a limited number of items such as fish or pebbles. Another list will also contain the different places the penguin can visit. The penguin will become hungry every certain number of turns, and will need to consume fish from the inventory to keep playing.

Sample interaction

Computer: You are at a mountain. There is a lake to the north. There is the ocean to the south.

User: Go north.

Computer: You are at the lake. You can fish or swim.

User: Swim.

Computer: You swim in the lake. You can keep swimming, fish, or leave.

User: Fish.

Computer: You catch 2 fish. You can keep fishing or leave.

User: Leave.

Computer: You get out of the lake. You are at the lake. There is a mountain to the south. There is a field of ice to the east.

User: What is in my inventory?

Computer: You have 2 fish and 1 pebble.

User: Drop a pebble.

Computer: You dropped the pebble. You are hungry. You have 2 fish.

User: Eat a fish.

Computer: You ate a fish. You have 1 fish left.


I may potentially add some of the following features if I have enough time or ability to complete them within the project time period, which would make the game a bit more immersive:
- Special events, such as a seal attack, meeting other penguins, or coming across a human.
- A data structure holding coordinates of places where the penguin has been to before, creating a "map" of the generated world to remember where they have been before.

Penguin needs:
- Hunger
- Energy
- HP
