"""dataclasses example"""
from dataclasses import dataclass


@dataclass
class Player:
    """A player in the game"""
    id: int
    name: str
    keys: set


# Example
if __name__ == '__main__':
    p1 = Player(1, 'Parzival', {'copper', 'jade'})
    print(repr(p1))
