from classes.property import Property
from classes.player import Player

class Board:
    def __init__(self, properties: list[Property], players: list[Player]):
        self.properties = properties
        self.players = players
        self.current_player_index = 0
        self.player_bankrupt = False

    def take_turn(self, roll: int) -> None:
        """Take a turn for the current player"""
        current_player = self.players[self.current_player_index]
        new_position = (current_player.position + roll) % len(self.properties)
        
        # Handle passing GO (This happens prior to the player paying rent)
        if new_position < current_player.position:
            current_player.money += 1
            
        current_player.position = new_position
        current_property = self.properties[current_player.position]
        
        # Check if player landed on GO
        if current_property.name == "GO":
            return
        # Check if player landed on a unowned property
        elif current_property.owner is None and current_property.price <= current_player.money:
            self._buy_property(current_player, current_property)
        # Check if player landed on an owned property
        elif current_property.owner is not None:
            self._pay_rent(current_player, current_property)

    def _buy_property(self, player: Player, property: Property) -> None:
        """Buy a property"""
        player.money -= property.price
        property.owner = player.name
        
        # Check if properties of the same colour are owned by the same player
        # Doing this here means it doesn't have to be done every time someone pays rent
        if self._check_color_set(player, property.colour):
            property.owns_color_set = True

    def _pay_rent(self, player: Player, property: Property) -> None:
        """Pay rent to the owner of a property"""
        rent_amount = property.price
        
        # Check if properties of the same colour are owned by the same player
        if property.owns_color_set:
            rent_amount *= 2

        player.money -= rent_amount
        self.players[property.owner].money += rent_amount
        
        if player.money <= 0:
            self.player_bankrupt = True

    def _check_color_set(self, player: Player, colour: str) -> bool:
        """Check if player owns all properties of a color"""
        color_properties = [p for p in self.properties if p.colour == colour]
        return all(p.owner == player for p in color_properties)
