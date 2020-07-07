"""Add __repr__ to Ride class and then loads rides from rides.pkl (pickle
format) and print repr of each ride.
"""
import pickle
from datetime import datetime


class Ride:
    def __init__(self, start, end, distance, num_passengers):
        self.start = start  # type: datetime
        self.end = end  # type: datetime
        self.distance = distance  # type: float
        self.num_passengers = num_passengers  # type: int

    def __repr__(self):
        cls = self.__class__.__name__
        # Short names for f-string
        start, end, dist = self.start, self.end, self.distance
        npass = self.num_passengers
        return f'{cls}({start!r}, {end!r}, {dist!r}, {npass!r})'


if __name__ == '__main__':
    with open('rides.pkl', 'rb') as fp:
        while True:
            try:
                ride = pickle.load(fp)
                print(ride)
            except EOFError:  # No more data
                break
