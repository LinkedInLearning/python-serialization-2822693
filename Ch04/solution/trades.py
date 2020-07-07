"""Write a protocol buffer definition file for a trade.
Then encode all trades and print out how many bytes it takes to encode all of
them.
"""
# Run the below to generate trade_pb2.py
#   protoc --python_out . trade.proto
import trade_pb2 as pb
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

size = 0
for obj in trades:
    trade = pb.Trade(
        symbol=obj['symbol'],
        volume=obj['volume'],
        price=obj['price'],
        buy=obj['buy'],
    )
    trade.time.FromDatetime(obj['time'])
    data = trade.SerializeToString()
    size += len(data)
print(f'total of {size} bytes')
