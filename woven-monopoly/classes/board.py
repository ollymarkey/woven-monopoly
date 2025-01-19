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
        elif current_property.owner is None:
            self._buy_property(current_player, current_property)
        # Check if player landed on an owned property
        elif current_property.owner is not None:
            self._pay_rent(current_player, current_property)

    def _buy_property(self, player: Player, property: Property) -> None:
        """Buy a property"""
        
        if player.money < property.price:
            print(f"{player.name} does not have enough money to buy {property.name}")
            return
        
        player.money -= property.price
        property.owner = player.id
        
        print(f"{self.players[player.id].name} bought {property.name}")
        
        # Check if properties of the same colour are owned by the same player
        # Doing this here means it doesn't have to be done every time someone pays rent
        self._check_colour_set(player, property.colour)

    def _pay_rent(self, player: Player, property: Property) -> None:
        """Pay rent to the owner of a property"""
        rent_amount = property.price
        property_owner = self.players[property.owner]
        
        # Check if properties of the same colour are owned by the same player
        if property.owns_colour_set:
            rent_amount *= 2

        print(f"{player.name} pays {rent_amount} to {property_owner.name}")
        player.money -= rent_amount
        property_owner.money += rent_amount
        
        if player.money <= 0:
            self.player_bankrupt = True

    def _check_colour_set(self, player: Player, colour: str) -> None:
        """Check if player owns all properties of a color"""
        truthy = True
        colour_properties = [p for p in self.properties if p.colour == colour]
        for property in colour_properties:
            if property.owner != player.id:
                truthy = False
                return truthy
        
        for property in colour_properties:
            property.owns_colour_set = True
            
        # Having to iterate over the colour properties again is not ideal, there is probably a better way to do this
        # But assuming that the board does not exceed the size of a monopoly board, this should be fine
        
        
