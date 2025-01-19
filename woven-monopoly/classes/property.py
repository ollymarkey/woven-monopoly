from typing import Optional

class Property:
    def __init__(
            self,
            id: int,
            name: str,
            type: str,
            price: Optional[int] = None,
            colour: Optional[str] = None,
            owner: Optional[int] = None
        ):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.colour = colour
        self.owner = owner
        self.owns_colour_set = False
        


