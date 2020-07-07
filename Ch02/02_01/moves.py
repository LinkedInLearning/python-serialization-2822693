"""Dance moves"""
from datetime import datetime, timedelta


class Move:
    """Move is a dance move"""
    def __init__(self, time, limb, what):
        self.time = time
        self.limb = limb
        self.what = what

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}({self.time!r}, {self.limb!r}, {self.what!r})'


# Dance moves
second = timedelta(seconds=1)
now = datetime.now()
move1 = Move(now + 1*second, 'jump', 'to the left')
move2 = Move(now + 2*second, 'step', 'to the right')
move3 = Move(now + 3*second, 'hands', 'on your hips')
move4 = Move(now + 4*second, 'knees', 'bring in tight')
