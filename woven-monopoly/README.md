# Woven Monopoly

This is an implementation of Woven Monopoly in python.

## System Design

The program is designed to be modular and extensible. There are three classes, `Property`, `Player`, and `Board`.
Each turn is initialized in `main.py`, with turns and game logic handled in `Board.py`.

## How to run

To run the program, use the following command:

```bash
python main.py
```

To run tests, use the following command:

```bash
python test.py
```

## Assumptions

1. If a player cannot afford to purchase an unowned property, they will not purchase it.
2. Rent is the same cost as the purchase price of the property.
3. Players draw if they have the same amount of money at the end of the game.
4. If no player is bankrupt after all dice rolls have been made, the game will end.
