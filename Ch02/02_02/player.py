"""repr example"""


class Player:
    """A player in the game"""
    def __init__(self, id, name, keys):
        self.id = id
        self.name = name
        self.keys = keys

    def __repr__(self):
        cls = self.__class__.__name__  # self can be a subclass
        return f'{cls}({self.id!r}, {self.name!r}, {self.keys!r})'


# Example
if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO, filename='game.log')

    p1 = Player(1, 'Parzival', {'copper', 'jade'})
    logging.info('p1 is %r', p1)
