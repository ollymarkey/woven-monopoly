import unittest
from main import load_board, load_players

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.players = load_players()
        self.board = load_board(self.players)
        
    # Test 1: Check that the correct number of properties are created
    def test_properties(self):
        self.assertEqual(len(self.board.properties), 9)
    
    # Test 2: GO is the first property
    def test_go(self):
        self.assertEqual(self.board.properties[0].name, "GO")
        
    # Test 3: Check that properties cannot be bought by a player that doesn't have enough money
    def test_buy_property(self):
        self.board.players[0].money = 0
        self.board._buy_property(self.board.players[0], self.board.properties[1])
        self.assertEqual(self.board.properties[1].owner, None)
    
    # Test 4: Check that rent doubles when a player owns all properties of a colour
    def test_rent_doubles(self):
        self.board.players[0].money = 10
        self.board.players[1].money = 10
        self.board._buy_property(self.board.players[0], self.board.properties[1])
        self.board._buy_property(self.board.players[0], self.board.properties[2])      
        self.board._pay_rent(self.board.players[1], self.board.properties[1])
        self.assertEqual(self.board.players[1].money, 8)
    
    # Test 5: Check that the game ends when a player goes bankrupt
    def test_game_ends(self):
        self.board.properties[1].owner = self.board.players[1].id
        self.board.players[0].money = 0
        self.board.take_turn(1)
        self.assertEqual(self.board.player_bankrupt, True)


if __name__ == "__main__":
    unittest.main()