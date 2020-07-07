"""namedtuple example"""
from collections import namedtuple

Player = namedtuple('Player', 'id name keys')

# Example
if __name__ == '__main__':
    p1 = Player(1, 'Parzival', {'copper', 'jade'})
    print(repr(p1))
