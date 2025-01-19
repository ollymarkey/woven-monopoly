from typing import Optional

class Property:
    def __init__(
            self,
            id: int,
            name: str,
            type: str,
            price: Optional[str] = None,
            colour: Optional[str] = None,
            owner: Optional[str] = None
        ):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.colour = colour
        self.owner = owner
        


