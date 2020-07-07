"""Write a protocol buffer definition file for a trade.
Then encode all trades and print out how many bytes it takes to encode all of
them.
"""
from datetime import datetime


def timestamp(s):
    """Convert timestamp string to datetime"""
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')


trades = [
    {
        'time': timestamp('2020-05-01T13:23:32'),
        'symbol': 'AAPL',
        'volume': 100,
        'price': 310.13,
        'buy': True,
    },
    {
        'time': timestamp('2020-05-02T15:17:24'),
        'symbol': 'MSFT',
        'volume': 20,
        'price': 184.69,
        'buy': False,
    },
    {
        'time': timestamp('2020-05-03T08:09:53'),
        'symbol': 'NFLX',
        'volume': 18,
        'price': 435.50,
        'buy': True,
    },
]
