"""Add __repr__ to Ride class and then loads rides from rides.pkl (pickle
format) and print repr of each ride.
"""
from datetime import datetime


class Ride:
    def __init__(self, start, end, distance, num_passengers):
        self.start = start  # type: datetime
        self.end = end  # type: datetime
        self.distance = distance  # type: float
        self.num_passengers = num_passengers  # type: int
