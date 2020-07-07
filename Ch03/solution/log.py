"""Print logs to standard output in JSON format, one object per line."""
import json
from dataclasses import dataclass, asdict
from datetime import datetime
from http import HTTPStatus
from ipaddress import IPv4Address


@dataclass
class Log:
    """A request log"""
    time: datetime
    ip: IPv4Address
    path: str
    status: HTTPStatus


logs = [
    Log(
        datetime(2020, 5, 1, 13, 23, 32),
        IPv4Address('163.206.89.4'),
        '/images/cat.png', 200,
    ),
    Log(
        datetime(2020, 5, 1, 13, 27, 1),
        IPv4Address('165.227.94.117'),
        '/images/dog.png', 200,
    ),
    Log(
        datetime(2020, 5, 1, 13, 32, 53),
        IPv4Address('137.204.201.12'),
        '/images/horse.png', 404,
    ),
    Log(
        datetime(2020, 5, 1, 13, 44, 2),
        IPv4Address('138.86.14.23'),
        '/images/cat.png', 200,
    ),
    Log(
        datetime(2020, 5, 1, 13, 51, 37),
        IPv4Address('142.130.48.163'),
        '/images/fox.png', 200,
    ),
]


def default(obj):
    """Convert datetime & IPv4Address to type supported by JSON"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, IPv4Address):
        return str(obj)
    return obj


for log in logs:
    data = json.dumps(asdict(log), default=default)
    print(data)
