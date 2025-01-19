"""
Play the game of Woven Monopoly
"""

import json
from classes.player import Player
from classes.property import Property
from classes.board import Board

# Constants
INITIAL_MONEY = 16
PLAYERS = [
    "Peter",
    "Billy",
    "Charlotte",
    "Sweedal"
]

def load_players():
    """Load the players from the constants provided"""
    players = []
    for i in range(len(PLAYERS)):
        players.append(Player(i, PLAYERS[i], INITIAL_MONEY))
    return players

def load_board(players: list[Player]):
    """Load the board configuration from board.json"""

    with open("../board.json", "r") as f:
        board_data = json.load(f)
            
    # Convert JSON data to Property objects
    properties = []
    for i, prop_data in enumerate(board_data):
        properties.append(
            Property(
                id=i,
                name=prop_data["name"],
                type=prop_data["type"],
                price=prop_data.get("price"),  # Using get() for optional fields
                colour=prop_data.get("colour"),
            )
        )
    
    return Board(properties, players)

    
def load_dice_rolls(game_number: int):
    """Load the dice rolls from dice_rolls.json"""    
    with open(f"../rolls_{game_number}.json", "r") as f:
        return json.load(f)

def start_game(board: Board, dice_rolls: list[int]):
    """Start the game"""
    MAX_ROLLS = len(dice_rolls)
    roll_count = 0
    while not board.player_bankrupt:
        # Take a turn
        board.take_turn(dice_rolls[roll_count])
        
        # Make sure we don't roll more than the number of rolls
        roll_count += 1
        if roll_count > MAX_ROLLS:
            break
        
        board.current_player_index = (board.current_player_index + 1) % len(board.players)
    
    # Handle the end of the game
    print("Game over!")
    winner = board.players[0]
    for player in board.players:
        print(f"{player.name} has ${player.money} left")
        if player.money > winner.money:
            winner = player
    
    print(f"{winner.name} wins with ${winner.money} left !!!")
    
    pass

if __name__ == "__main__":
    # Initialise the board and dice rolls
    players = load_players()
    board = load_board(players)
    
    # Play game 1 with rolls_1.json
    dice_rolls = load_dice_rolls(1)
    print("Game 1:")
    start_game(board, dice_rolls)
    
    # Reset the board and players
    players = load_players()
    board = load_board(players)
    
    # Play game 2 with rolls_2.json
    dice_rolls = load_dice_rolls(2)
    print("Game 2:")
    start_game(board, dice_rolls)
